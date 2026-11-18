# Lecture entière d'EvoSCM (arXiv 2609.01526 v2) contre O4 : PDF et code — v1

- **Lecteur : modèle I.** Pièce voisine de O4 (juge au nul formé des lois connues). Cette note vérifie la lecture v2 du modèle C (lecture-pdf-priorite-haute-o4-v2.md, section 3.5) ; elle ne la recopie pas et ne la remplace pas (R12).
- **Heures (date -u, recopiées)** : début (vérification du PDF et du clone) 2026-11-18T01:42:48Z ; extraction et lecture des pages à partir de 01:42:56Z ; recherche de termes sur le PDF 01:45:21Z ; liste des fichiers du clone 01:45:33Z ; empreintes des fichiers du clone 01:54:28Z ; rejeu des extraits de code 01:55:20Z ; début de rédaction 01:56:19Z ; rejeu final des deux listes, après corrections de la note, 2026-11-18T02:00:18Z.
- **PDF** : docs/sources/pdf/lecture-o4-v2/arxiv-2609.01526/2609.01526.pdf, 34 pages, sha256 4094a67b0dddba479f4fd4d3a01ad03b05e4c93a255956516130f1153296cf98 (recalculé, conforme). Zhao, Li, Deng, Yang, Wei, Lin, EvoSCM, arXiv 2609.01526v2, daté du 28 septembre 2026 sur la p. 1.
- **Code** : clone en lecture seule code-o4/EvoSCM, origine https://github.com/evoscm/EvoSCM, commit ffb638998da9537d738c20176ad928319889ff96 (vérifié par git rev-parse HEAD ; dernier commit daté du 12 octobre 2026, message d'une ligne — date et message lus par git log, non cités du PDF). 52 fichiers suivis. Licence MIT. Aucun programme du clone n'a été lancé. Provenance et empreintes : docs/sources/code/lecture-o4-v1/evoscm/provenance-v1.md.
- **Profondeurs** : PDF lu en entier, p. 1 à 34 (section 1). Code : lu en entier pour les fichiers qui réalisent la proposition, le calcul des poids, la sélection, le retrait, l'engagement des prédictions et la finalisation ; le reste parcouru par structure et recherche ciblée (section 1, table 2).
- **Rejeux** : citations du PDF **46 sur 46** (lecture-entiere-evoscm-o4-v1-resultat-citations-pdf.json, programme verifier_citations_priorite_haute_o4_v1.py inchangé) ; extraits de code **42 sur 42** (lecture-entiere-evoscm-o4-v1-resultat-extraits-code.json, programme verifier_extraits_code_o4_v1.py inchangé, code de sortie 0). Chaque passage entre guillemets de cette note est dans l'une des deux listes.
- **Règles** : R7 (rien de mémoire), R8 (non trouvé = dans ce qui est lu, à la profondeur dite), N-067 (le verdict en vigueur sur O4 reste **occupée en partie** ; tout écart est un nœud pour Lazar, section 8), R4 (en cas de doute, le sens non flatteur pour notre revendication).

## 1. Profondeurs

### 1.1 PDF

| pages | contenu | lecture |
|---|---|---|
| 1-10 | résumé, introduction, travaux liés, méthode (§ 3), expériences (§ 4), conclusion, déclaration d'usage de l'IA | en entier, page par page (pdftotext -layout -f N -l N) |
| 10-13 | références | en entier |
| 14 | table des annexes | en entier |
| 15-19 | annexes A et B (résultats, jetons, ablations, études de cas) | en entier ; les figures 5 (p. 17), 6 (p. 18), 7 et 8 (p. 19) lues par leur texte extrait, les tracés eux-mêmes non lus |
| 20-22 | annexe C (représentation, invites) | en entier |
| 23 | algorithme 1 et annexe D.1 | en entier |
| 24-26 | annexes D.2, D.3 | en entier |
| 26-32 | annexe E (détails d'expérience par banc) | en entier |
| 32-33 | annexe F (monde Yukawa) | en entier ; dérivations suivies, non revérifiées |
| 33-34 | annexe G (travaux liés) | en entier |

Aucune page sautée. Les figures sont lues par le texte que pdftotext en extrait ; une information portée seulement par un tracé n'est pas lue.

### 1.2 Code (commit ffb63899…)

| fichier | lignes | lecture |
|---|---|---|
| ScienceAgent/scienceagent/scm_pipeline.py | 4455 | **en entier** : l. 1-80, 390-680, 1480-1560, 1703-1930, 2101-2170, 2237-2264, 2382-2470, 2560-2600, 2775-2805, 2979-4455 (ingestion des réponses, candidats, retrait, sélection des plans, exécution, validation des prédictions, postérieur, métriques, export). **Parcouru par recherche ciblée** : l. 80-390 (ajustements de mécanismes nommés), 680-1480 et 1560-1700 (audit causal), 1930-2100, 2170-2236, 2264-2380, 2470-2560, 2600-2775, 2805-2978 (audits et lois déduites). |
| ScienceAgent/scienceagent/agent.py | 1310 | en entier |
| ScienceAgent/scienceagent/release.py, llm_client.py, response_protocol.py, responses_transport.py | 187, 73, 38, 34 | en entier (llm_client.py affiché avec les noms de clés masqués à l'écran ; aucune valeur de clé n'existe dans le fichier) |
| ScienceAgent/scienceagent/transfer.py | 179 | l. 1-140 ; reste par recherche |
| ScienceAgent/scienceagent/trajectory_logger.py | 327 | l. 1-120 et structure |
| ScienceAgent/scienceagent/context_window.py | 369 | l. 320-369 et recherche des empreintes |
| PhysicsSchool/prompts/scm_protocol.md, _template_interactive.md | 494, 74 | en entier |
| configs/baseline/gpt55.yaml, configs/evoscm/gpt55.yaml, scripts/run_discovery.py, run_benchmark.py, evaluate.py, smoke_test.py, LICENSE, environment.yml, .gitignore | — | en entier |
| .env.example | 5 | noms de variables seulement, valeurs masquées à l'affichage |
| README.md | 143 | l. 20-110 ; reste par recherche |
| tests/test_scm_pipeline.py | 2049 | l. 180-270 et 1694-1900 (essais du postérieur, du retrait, de l'équivalence des prédictions) ; reste par recherche |
| evaluator.py, executor.py, worlds.py, mse_fitting.py, load_trajectories.py, PhysicsSchool/physchool/*, autres invites d'instructions, autres essais, scripts/run_transfer.py, setup.py | — | **parcourus** par structure (fonctions et classes) et recherche de termes ; non lus ligne à ligne |
| assets/figures/*.webp | — | non lus (images) |

Le clone ne contient que le banc de physique (DiscoverPhysics) : la table des mondes du lancement (release.py, l. 20-32) ne compte que les onze mondes publics de physique, et aucun fichier ne porte le code des bancs de chimie (LLEMA) ou de réseaux de gènes (ActiveSciBench-GRN). Ce que le PDF décrit pour ces deux bancs (p. 28-32) est donc **lu sur le PDF seulement, non vérifiable sur le code**.

## 2. Recherche de termes

### 2.1 PDF (texte entier, 34 pages, casse ignorée)

| terme | occurrences | pages | ce que c'est |
|---|---|---|---|
| e-value, e-process, anytime, martingale, optional stopping, stopping, sequential test | 0 | — | — |
| sequential | 2 | 11, 26 | référence bibliographique (p. 11, voir plus bas) et une cascade d'activation d'un motif génétique (p. 26) ; aucun test séquentiel |
| likelihood ratio, likelihood, Bayes factor | 0 | — | le mot likelihood ne figure nulle part dans le PDF |
| encompass, incremental | 0 | — | — |
| spanning | 3 | 28, 33, 34 | sens courant (étendue d'un balayage de rayons ; étendue d'une littérature) ; aucun test de recouvrement |
| marginal | 1 | 16 | un léger surcroît de consommation de jetons |
| benchmark | 22 | 6-33 | les trois bancs d'essai |
| baseline | 42 | 1-31 | l'agent de base de chaque banc, comparé à EvoSCM ; jamais une loi de référence à battre |
| null | 1 | 27 | intervention à source nulle (charge source mise à zéro) : un nul physique, pas statistique |
| multiple testing, false discovery, Bonferroni, Holm | 0 | — | — |
| pre-regist, preregist, hash, seal | 0 | — | — |
| pre-commit | 8 | 17, 18, 22, 27, 29 | engagement des prédictions avant l'issue (section 3) |
| posterior | 5 | 8, 9, 18, 27 | entropie et poids a posteriori, cotes a posteriori (section 3) |
| threshold | 2 | 18, 25 | seuil d'acceptation des relations (p. 18) ; seuil d'énergie au-dessus de l'enveloppe du banc de matériaux (p. 25) |
| significan, p-value | 0 | — | — |

Une référence mérite d'être relevée : la bibliographie cite Huang et al. 2025, [p. 11] « Automated hypothesis validation with agentic sequential falsifications » (l'agent de falsification séquentielle que N-064 donne comme occupant en partie les e-valeurs hors des agents). Le texte ne la cite qu'en passant, parmi les systèmes qui automatisent la recherche : [p. 3] « Recent systems automate parts of the scientific pipeline (Boiko et al., 2023; Lu et al., 2024; Huang et al., 2025) ». EvoSCM ne reprend pas sa statistique dans ce qui est lu.

### 2.2 Code (52 fichiers suivis, images exclues, casse ignorée)

e-process, anytime, martingale, optional stopping, likelihood ratio, Bayes factor, Bonferroni, Holm, false discovery, p-value, encompass, seal, timestamp : **zéro**. e-value : une seule occurrence, fausse (dans un mot du protocole, positive-valued, qui contient cette suite de lettres) ; e_value : faux positifs (noms de variables qui finissent par time_value). sequential : une occurrence (le lisez-moi : les courses sont lancées l'une après l'autre). baseline : l'agent de base et ses fichiers de configuration. null : l'intervention à source nulle et les valeurs nulles de JSON. preregist, pre-regist, commit : vocabulaire de l'engagement des prédictions (section 4). hash : la bibliothèque hashlib, importée en deux endroits (section 4.4).

## 3. Lecture du PDF par composante

**P (juger une proposition contre le connu, non contre aucun effet).** Le PDF met des hypothèses en concurrence entre elles : [p. 1] « Competing SCM hypotheses make falsifiable predictions and guide discriminative experiments that separate alternative explanations. » La loi familière est mise à égalité au départ, non posée comme nul : [p. 27] « with uniform evidence weights, irrespective of any confidence values reported by the LLM », [p. 27] « to avoid favoring a familiar textbook law before any experiment has been performed » ; et le programme ne lui fait pas confiance : [p. 27] « the runtime tracks a set of systematic audits rather than trusting the most familiar initial law », audits dont le premier est [p. 27] « These include a null-source intervention ». La sélection entre concurrentes est dite décisive : [p. 18] « enabling decisive model selection », [p. 18] « Posterior odds: finite / vanishing », [p. 18] « Pre-committed predictions favor the finite-core hypothesis ». Ce n'est pas un jugement contre une archive de lois connues : la base de comparaison des tableaux est un agent, [p. 6] « Each benchmark domain provides a baseline agent implementing the domain-specific experimental loop ». **Voisin.**

**(i) Proposeurs modèles de langue.** [p. 10] « EvoSCM uses LLMs as the reasoning backbone of scientific agents, performing abductive inference, causal experiment design, inductive rule extraction, structural revision, and deductive validation » ; [p. 27] « At each round, the LLM proposes two to four candidate experiment designs together with pre-committed predictions from the competing hypotheses. » Deux bornes : sur le banc de matériaux, [p. 29] « Each hypothesis is a bootstrap sparse ridge mechanism fitted independently for each property outcome. » ; sur le banc de gènes, les hypothèses viennent d'une grammaire publique, [p. 20] « Because coherent and incoherent motifs both belong to the public candidate grammar », et [p. 31] « it is not unconstrained de novo topology discovery ». **Pris** (banc de physique) ; voisin sur les deux autres bancs.

**(ii) Nul = mise en commun ajustée des lois prédictives de l'archive.** Le PDF parle d'une population pondérée, [p. 9] « concentrating posterior weight on hypotheses that best explain the evidence », [p. 8] « These informative experiments translate into consistently larger SCM posterior entropy reductions », et d'une agrégation en fin de course, [p. 6] « predictions are aggregated into a consensus outcome ». C'est un mélange des hypothèses de l'agent, non une archive de lois connues, et il ne sert pas de nul. **Voisin (lointain)** ; le nul formé de l'archive n'est pas trouvé.

**(iii) e-processus comme règle de promotion.** Zéro occurrence des termes (section 2.1). Les cotes a posteriori de la p. 18 sont une étude de cas ; le PDF ne dit pas comment les poids sont calculés. Le seul seuil d'acceptation est celui des relations du banc de matériaux : [p. 18] « their estimated reliability remains below the acceptance threshold », [p. 29] « Outcome-specific edges are withheld from the planner when their calibrated reliability falls below 0.20 ». **Voisin** (règle à seuil sur une fiabilité, sans garantie d'erreur ; voir les réponses en section 5).

**(iv-a) Prédictions engagées avant que les données existent.** [p. 5] « Before executing the intervention, the agent commits to a falsifiable, hypothesis-specific prediction for each candidate. », [p. 5] « These predictions are recorded prior to experimentation », [p. 5] « it prevents post-hoc rationalization » ; invite : [p. 22] « Commit to a specific numerical prediction before observing the experimental result. » ; ablation : [p. 17] « w/o Pre-committed Prediction (Only Observations) », [p. 17] « Without pre-commitment, the agent can rationalize any observation post-hoc ». Sur les deux autres bancs : [p. 30] « every prediction is stored before its outcome is observed », [p. 31] « Each hypothesis’s reporter predictions are committed before the selected experiments are submitted to the simulator. » Point que la v2 ne relevait pas : sur le banc de physique, les données n'existent pas avant l'expérience, [p. 23] « Observations are generated on demand rather than retrieved from a fixed dataset. » L'engagement précède donc l'existence des données, dans un monde simulé ([p. 10] « Our evaluation focuses on simulated scientific environments. »). Aucun scellement : hash et seal donnent zéro occurrence ; la seule empreinte du texte porte sur un cache d'oracle, [p. 30] « Cache keys depend on the CIF bytes, property model, and oracle version. » (le mot empreinte n'y est pas écrit ; la page dit seulement de quoi dépend la clé). Sur le banc de gènes, le graphe choisi est gelé avant l'évaluation, [p. 32] « The selected graph is frozen before the evaluator is invoked », choisi par [p. 32] « five-fold grouped cross-validation using the mean held-out squared log error » : un gel avant la note, pas une prédiction scellée. **Voisin** : engagement avant l'existence des données, pris ; scellement, non trouvé.

**(iv-b) Statistique calculée hors des agents.** [p. 27] « the runtime supplies a compact JSON state containing the current hypothesis population, posterior weights, recent prediction errors » ; [p. 27] « EvoSCM executes only the feasible design with the largest posterior-weighted predictive disagreement » ; [p. 28] « against observation-derived causal evidence before accepting the submission ». Mais la validation des hypothèses révisées est faite par l'agent : [p. 5] « Evidence Validation: the agent derives predictions from », [p. 5] « Hypotheses that pass both checks are retained ». Le PDF renvoie au code pour les détails : [p. 21] « full prompt templates are included in the released code », [p. 27] « Complete prompt templates and schemas are included in the released code. » La note des explications est confiée à un modèle de langue commercial : [p. 24] « Explanation quality is evaluated separately by an LLM judge using an expert-written, world-specific rubric » (c'est la mesure du banc, non une règle de la boucle). Sur pièce, le mode de calcul des poids n'est pas dans le PDF ; il est dans le code (section 4).

## 4. Lecture du code

Tout ce qui suit porte sur le commit ffb638998da9537d738c20176ad928319889ff96, banc de physique seulement.

### 4.1 Qui propose, qui calcule

Les candidates et les prédictions viennent de la réponse du modèle de langue, analysée par le programme avant toute exécution : agent.py l. 215-217 « scm_round = self.scm_pipeline.ingest_reply( reply, round_num, max_episode_cost=self.remaining_simulator_episodes ) ». Les poids, la sélection du plan, le retrait et le contrôle final sont calculés par le programme (4.2 à 4.5). La déduction n'est pas un contrôle du programme : elle est enregistrée comme texte de l'agent, scm_pipeline.py l. 3228-3231 « for deduction in _as_list(update.get("deductions")): self.deductions.append( {"round": round_num, "content": _jsonable(deduction)} ) ».

### 4.2 Calcul des poids a posteriori (scm_pipeline.py, _validate_predictions et posterior)

1. Écart standardisé par l'incertitude que le modèle déclare lui-même : l. 4022-4023 « z_score = rmse / prediction["sigma"] » ; classement à seuils fixes, l. 4024-4029 « if z_score <= 1.0: status = "success" elif z_score <= 3.0: status = "tension" else: status = "counterexample" ».
2. Log-vraisemblance gaussienne, bornée : l. 4030-4033 « log_likelihood = float( -0.5 * z_score**2 - math.log(prediction["sigma"]) ) log_likelihood = min(max(log_likelihood, -50.0), 20.0) ». L'invite l'annonce : scm_protocol.md l. 248-249 « Predictions are scored with a Gaussian proper score. »
3. Regroupement des prédictions presque égales, qui reçoivent la même évidence : l. 4101-4102 « if disagreement < self.min_disagreement_z: union(left_index, right_index) », avec par défaut (l. 532-535) « max_candidates: int = 8, complexity_penalty: float = 0.25, evidence_temperature: float = 0.7, min_disagreement_z: float = 0.5, ».
4. Évidence **relative au meilleur groupe** pour la même cible : l. 4123 « relative = (group_scores[root] - best) * causal_weight » (le poids causal vaut 1 pour un effet apparié ou sans bruit, 0,25 sinon : l. 4116-4121, non cité).
5. Agrégation par hypothèse, tempérée : l. 4132-4136 « relative_log_evidence = ( float(np.mean(relative_values)) * math.sqrt(len(relative_values)) * self.evidence_temperature ) », ajoutée aux log-poids : l. 4143-4145 « self.log_weights[hypothesis_id] = ( self.log_weights.get(hypothesis_id, 0.0) + relative_log_evidence ) », puis renormalisée (l. 4146, 4213-4237).
6. Le postérieur affiché et utilisé retranche une pénalité de complexité : l. 4194-4196 « self.log_weights.get(candidate_id, 0.0) - self.complexity_penalty * self._candidate_complexity(self.candidates[candidate_id]) ». L'invite parle d'une loi a priori de longueur de description minimale (scm_protocol.md l. 182-185, non citée).
7. Poids d'entrée : l. 3281-3285 « if uniform_prior: entry_weight = 0.0 else: entry_weight = math.log(confidence) ». Uniforme pour la population du premier tour seulement (l'invite, l. 103-106 : « Round-one candidate weights are deliberately initialized uniformly: a commonsense `confidence` is recorded for audit but is not observational evidence. ») ; une candidate ajoutée plus tard entre avec le logarithme de la confiance que le modèle de langue déclare.

Ce n'est ni un rapport de vraisemblance cumulé ni une e-valeur : la moyenne multipliée par la racine du nombre de cibles, la température 0,7, la pénalité de complexité, la borne [-50, 20] et l'incertitude choisie par le modèle font une note de classement, sans garantie d'erreur déclarée.

### 4.3 Sélection du plan d'expérience

Score d'information : désaccord standardisé pondéré par le produit des postérieurs, divisé par la racine du coût, l. 3767-3772 « pair_weight = posterior.get( left["hypothesis_id"], 0.0 ) * posterior.get(right["hypothesis_id"], 0.0) score += causal_weight * pair_weight * disagreement cost = self._design_episode_cost(design) score /= math.sqrt(cost) » ; choix du maximum parmi les plans restants, l. 3715-3717 « selected_index = max( feasible_indices, key=lambda idx: (scores[idx]["information_score"], -idx) ) ». Avant ce choix, le programme filtre les plans par les audits obligatoires (l. 3650-3714 : source nulle, signes, amplitude de la seconde charge, rayons, phase). Le PDF (p. 27) ne dit que le maximum de désaccord ; le code y ajoute ces filtres.

### 4.4 Engagement des prédictions avant l'issue, et sa trace

- Ordre imposé par le programme : analyse de la réponse (agent.py l. 215-217), puis exécution, l. 368 « execution = self.scm_pipeline.execute_pending(self.executor) », puis validation, l. 388 « validation = self.scm_pipeline.validate_pending(execution) ». Les prédictions sont copiées au choix du plan, scm_pipeline.py l. 3724 « predictions=copy.deepcopy(selected["predictions"]), », et versées au dossier d'évidence seulement après l'issue, l. 4054 « self.evidence.append(record) ».
- L'engagement n'est pas obligatoire : une expérience peut tourner sans prédiction, et la validation le note, l. 4156 « "uncommitted": len(predictions) == 0, ». L'indicateur dit de préenregistrement vaut vrai dès qu'une prédiction a été notée, l. 4368 « "preregistered_prediction": bool(self.evidence), ». L'invite parle de préenregistrement : scm_protocol.md l. 7 « pre-registered predictions against simulator observations. »
- **Aucune trace cryptographique ni horodatage des prédictions.** Une fonction d'empreinte existe, scm_pipeline.py l. 38 « def _canonical_sha256(value: Any) -> str: », mais elle n'est appelée nulle part dans le clone (recherche sur tous les fichiers : seule sa définition) ; agent.py l. 2 « import hashlib » est importé sans usage trouvé. Les seules empreintes calculées portent sur les messages omis lors du compactage du contexte (context_window.py l. 354-358). Aucun horodatage par prédiction ; l'identifiant de course porte l'heure de lancement (trajectory_logger.py l. 31-35, non cité). Le journal des trajectoires ne contient que les entrées et sorties d'expérience, dans un dossier temporaire, release.py l. 109 « with tempfile.TemporaryDirectory(prefix="evoscm-") as temporary: » ; l'état complet, prédictions comprises, n'est écrit qu'en fin de séance (release.py l. 151-172 et save_json, non cités).

### 4.5 Règles à seuil : retrait, capacité, contrôle final, bibliothèque de lois

- **Retrait** d'une hypothèse demandé par le modèle, accordé par le programme seulement si : l. 3412-3413 « if len(counterexample_designs) >= 2 and paired_counterexample: return True », ou l. 3423 « return len(distinct_designs) >= 3 and cumulative <= -3.0 ». L'invite l'annonce, scm_protocol.md l. 173-176 « The runtime accepts retirement only after counterexamples from at least two distinct designs including a noise-cancelled paired-effect falsification *and negative relative evidence against competing candidates* ». C'est la règle la plus proche d'une règle séquentielle à seuil dans le code : évidence relative cumulée contre la meilleure concurrente, seuil -3,0, sur au moins trois plans. Elle décide d'un retrait, pas d'une promotion, et n'a pas de garantie d'erreur.
- **Capacité** : au-delà de la capacité, les plus faibles poids sortent, l. 3303 « candidate["status"] = "retired_capacity" ».
- **Contrôle exécutable de la loi finale** : réussite si l. 1897-1899 « passed = bool( median_error <= 0.35 and p80_error <= 0.75 and mechanism_consistent ) » ; réussite par défaut sans données, l. 1732-1734 « "available": False, "passed": True, "reason": "no reliable null-anchored two-particle responses", ». En cas d'échec, deux tours de réparation, agent.py l. 987 « for attempt in range(1, 3): », puis la meilleure loi est rendue de toute façon, l. 1050 « return (best_law, best_explanation) ». Ce n'est pas un refus de la loi.
- **Bibliothèque de lois nommées tenue par le programme** : le programme ajuste lui-même des familles connues (écran de Helmholtz à noyau de Bessel, somme d'images d'une dimension compactifiée, loi de puissance, modulation sinusoïdale ; l. 80-390) aux réponses mesurées et en déclare une choisie si l'ajustement passe un seuil, l. 1513-1514 « screened_helmholtz_fit is not None and screened_helmholtz_fit["relative_log_rmse"] < 0.12 », en écrivant à l'agent l. 1519-1520 « the controlled radial response quantitatively selects a static two-dimensional screened Helmholtz/Yukawa field ». C'est une bibliothèque de lois connues ajustée par le programme, servie comme **correspondance proposée** à l'agent (et, pour la somme d'images et la modulation, comme loi finale de substitution dans la réparation, agent.py l. 840-860, non cité) ; ce n'est pas un nul à battre.
- **Choix final** : par le modèle de langue (champ du candidat choisi dans le bloc final) ; à l'export, le programme ne retombe sur le plus fort postérieur que si ce choix est invalide, transfer.py l. 84 « selected_id = claim.get("selected_candidate_id") » et l. 94-96 « selection_basis = "highest_posterior_fallback" else: selection_basis = "final_claim" ».

## 5. Réponses aux questions propres à la pièce

1. **Comment les poids a posteriori sont-ils calculés ?** Par le programme, non par le modèle de langue : log-vraisemblance gaussienne de l'erreur quadratique moyenne divisée par l'incertitude que le modèle déclare (l. 4022-4033), rendue relative au meilleur groupe de prédictions sur la même cible (l. 4123), agrégée en moyenne fois racine du nombre, tempérée par 0,7 (l. 4132-4136), cumulée dans les log-poids (l. 4143-4145) ; le postérieur retranche 0,25 fois une mesure de complexité (l. 4194-4196). Deux entrées viennent du modèle : la moyenne et l'incertitude de chaque prédiction, et la confiance déclarée d'une candidate ajoutée après le premier tour (l. 3281-3285). Le PDF ne le dit pas (zéro occurrence du mot likelihood).
2. **Les prédictions sont-elles stockées avant l'issue, avec quelle trace ?** Oui, en mémoire, par l'ordre du programme (analyse, exécution, validation : agent.py l. 215-217, 368, 388 ; copie l. 3724). Trace : **rien** au moment de l'engagement — ni empreinte (la fonction d'empreinte n'est jamais appelée), ni horodatage ; écriture sur disque en fin de séance seulement. L'engagement n'est pas obligatoire (l. 4156).
3. **Règle d'acceptation d'une hypothèse contre la loi en vigueur ou familière, avec seuil ?** Non trouvée. Il y a des seuils de **retrait** (l. 3412-3413, 3423), de **capacité** (l. 3303), de **réussite d'un contrôle exécutable** qui ne refuse pas (l. 1897-1899, 987, 1050), de **sélection d'une loi nommée** dans la bibliothèque du programme (l. 1513-1514), et des audits obligatoires qui retardent la loi finale. La loi familière n'est qu'une candidate parmi d'autres, à poids égal au premier tour.
4. **Que fait exactement le seuil de fiabilité 0,20 ?** Sur le PDF : sur le banc de matériaux seulement, il retire au planificateur les arêtes dont la fiabilité calibrée passe sous 0,20, [p. 29] « Outcome-specific edges are withheld from the planner when their calibrated reliability falls below 0.20 » ; fiabilités de départ [p. 29] « The numerical SCM starts with a reliability prior of 0.15, while the LLM chemistry prior is initialized at 0.25. », mises à jour selon [p. 29] « Reliability is updated using pre-committed prediction error and parent-child delta-sign accuracy. » (formule non donnée). Le seuil d'acceptation de la p. 18 est probablement le même ; la page ne le dit pas. Sur le code : **non vérifiable**, le code de ce banc n'est pas dans le clone (aucune occurrence de reliab ni de 0.20 dans ce sens).
5. **e-valeur, rapport de vraisemblance séquentiel, validité à tout instant d'arrêt, contrôle d'erreur ?** Aucun, ni dans le PDF (section 2.1) ni dans le code (section 2.2). Le plus proche est la règle de retrait (évidence relative cumulée, seuil -3,0), sans garantie.
6. **Le code confirme-t-il ou contredit-il le PDF ?**
   - **Confirme** : l'engagement avant l'issue (p. 5, 22, 27) ; les poids uniformes du premier tour (p. 27) ; le choix du plan par désaccord pondéré par le postérieur (p. 27), avec en plus le filtre des audits et la division par la racine du coût ; des poids et un état tenus par le programme (p. 27).
   - **Contredit ou nuance** : (a) la taille maximale de population est [p. 27] « The maximum population size is Kmax = 6. », alors que le code donne 8 par défaut (l. 532 ; release.py l. 79 « scm_max_candidates=8, » ; README.md l. 96 « | SCM capacity | 8 | ») ; (b) l'algorithme 1 et la p. 5 écartent les hypothèses qui échouent à la déduction ; dans le code, la déduction n'est que du texte enregistré (l. 3228-3231) et une hypothèse ne sort que par retrait accordé ou par capacité ; (c) l'agrégation en consensus de la p. 6 n'est pas trouvée dans le code (recherche de consensus, aggregat, mixture, ensemble : zéro) ; (d) la p. 28 dit le contrôle fait [p. 28] « against observation-derived causal evidence before accepting the submission » ; le code répare puis rend la loi (agent.py l. 987, 1050) et réussit par défaut sans données (l. 1732-1734) ; (e) la p. 28 dit [p. 28] « These quantities are returned as evidence summaries; no hidden world label or ground-truth equation is used. » : aucune étiquette de monde n'est lue dans ce qui est lu, mais le programme tient une bibliothèque de familles de lois nommées (4.5) dont deux correspondent à des mondes publics du banc (écran de Yukawa, dimension compactifiée : p. 24, table 12) — information sur la validité des résultats d'EvoSCM, hors O4 ; (f) l'invite dit regrouper les prédictions qui diffèrent de moins de leur incertitude commune, scm_protocol.md l. 253-254 « Predictions that differ by less than their pooled uncertainty are treated as one empirically equivalent group », le code le fait à 0,5 de cette incertitude (l. 4101-4102, l. 535) : écart mineur entre invite et code.
   - **Non vérifiable** : tout ce qui touche les bancs de matériaux et de gènes, dont le seuil 0,20 et le gel du graphe.

## 6. Table pris, voisin, non trouvé d'EVOSCM

| composante | statut | preuve |
|---|---|---|
| **P** | **voisin** | concurrentes jugées l'une contre l'autre, relativement à la meilleure (l. 4123) ; loi familière à poids égal au départ (p. 27 ; l. 3281-3285) ; audits obligatoires au lieu de la confiance dans la loi familière (p. 27) ; bibliothèque de lois nommées ajustée par le programme, servie comme correspondance (l. 1513-1520). Aucune proposition jugée contre ce qu'une archive de lois prédit déjà. |
| **(i)** | **pris** (physique) ; voisin (matériaux, gènes) | p. 10, 27 ; agent.py l. 215-217 ; p. 29 (régressions ridge), p. 20, 31 (grammaire publique) |
| **(ii)** | **voisin (lointain)** ; nul formé de l'archive non trouvé | population pondérée (p. 9 ; l. 4194-4196) ; bibliothèque de lois connues ajustées séparément, choix à seuil 0,12 (l. 1513-1514), sans mise en commun ni rôle de nul ; consensus de la p. 6 non trouvé dans le code |
| **(iii)** | **voisin** ; e-processus non trouvé | log-score gaussien relatif cumulé et tempéré (l. 4123, 4132-4136, 4143-4145) ; retrait au seuil -3,0 sur trois plans (l. 3423) ; zéro occurrence des termes (PDF et code) |
| **(iv-a)** | **voisin** : engagement avant l'existence des données **pris** (simulation à la demande, p. 23 ; ordre imposé, agent.py l. 215-217, 368, 388) ; scellement **non trouvé** | fonction d'empreinte jamais appelée (l. 38) ; aucun horodatage ; engagement facultatif (l. 4156) |
| **(iv-b)** | **pris** pour la statistique (postérieur calculé par le programme) ; **voisin** pour une statistique de promotion | l. 4022-4146, 4194-4196 ; retrait accordé par le programme (l. 3412-3423) ; mais déduction faite par l'agent (p. 5 ; l. 3228-3231) et choix final par le modèle (transfer.py l. 84, 94-96) |
| **Conjonction** | **non trouvée** dans ce qui est lu | pas de nul formé de l'archive, pas d'e-processus ni de garantie d'erreur, pas de scellement, pas de règle de promotion contre la loi en vigueur |

## 7. Changements par rapport à la v2 (lecture-pdf-priorite-haute-o4-v2.md, section 3.5 et ligne EVOSCM de la section 4)

| constat de la v2 | cette lecture | effet |
|---|---|---|
| Profondeur : p. 18, 27, 28, 29 en entier ; 5, 17, 30 par lignes ; code non lu | p. 1-34 en entier ; code lu pour les parties décisives (section 1.2) | profondeur étendue ; les constats non trouvés de la v2 sont maintenant bornés par le PDF entier |
| La v2 (section 3.5) notait que le PDF ne dit pas comment les poids a posteriori sont calculés, le mot likelihood n'y figurant pas | confirmé sur le PDF ; **répondu par le code** (section 5, point 1) | nœud 2 de la v2 répondu pour le banc de physique |
| La v2 donnait les poids comme tenus hors du modèle de langue (citation des poids uniformes, p. 27) | vrai pour le calcul ; **inexact en général** : uniforme au premier tour seulement ; une candidate ajoutée ensuite entre avec la confiance déclarée par le modèle (l. 3284) ; l'incertitude de chaque prédiction, choisie par le modèle, entre dans la vraisemblance | précision, dans le sens qui éloigne EvoSCM d'une statistique entièrement hors des agents |
| (iv-b) **voisin** | **pris** pour la statistique (le postérieur est calculé par le programme) ; voisin pour une statistique de promotion | changement de statut, dans le sens non flatteur pour O4 (R4) ; nœud 1 |
| (iv-a) voisin ; la v2 disait l'engagement fait par l'agent, dans un journal, sans empreinte | voisin, maintenu ; précisé : l'ordre est imposé **par le programme** (non par l'agent), les données du banc de physique n'existent pas avant l'expérience (p. 23), aucune trace au moment de l'engagement, fonction d'empreinte présente mais jamais appelée, engagement facultatif | renforcé quant à l'engagement, inchangé quant au scellement |
| La v2 lisait p. 28 un contrôle par le programme avant d'accepter la loi finale | le code **ne refuse pas** : réparation en deux tours puis loi rendue ; réussite par défaut sans données | correction de lecture ; affaiblit le caractère de porte du contrôle |
| (iii) voisin (cotes a posteriori p. 18 ; seuil 0,20 p. 29) | voisin, maintenu ; s'y ajoute la règle de retrait du code (seuil -3,0 sur l'évidence relative cumulée), la plus proche d'une règle séquentielle à seuil, sans garantie | précision ; nœud 2 |
| Seuil 0,20 : retient les arêtes pour le planificateur, pas une promotion | confirmé sur le PDF ; **non vérifiable sur le code** (banc absent du clone) | inchangé, borné |
| (ii) voisin (population pondérée) | voisin (lointain), maintenu ; s'y ajoute une bibliothèque de lois connues ajustée par le programme, qui sert de correspondance et non de nul | précision |
| P voisin (loi familière à poids égaux) | voisin, maintenu ; comparaison relative à la meilleure concurrente | inchangé |
| (i) pris, voisin sur le banc de matériaux | pris sur le banc de physique, voisin sur les deux autres (grammaire publique du banc de gènes ajoutée) | précision |
| — | PDF et code divergent sur la taille maximale de population (6 contre 8), sur l'élimination par déduction, sur le consensus | nouveau ; information |
| — | la bibliographie cite l'agent de falsification séquentielle de Huang et al. 2025 (p. 3, 11) sans en reprendre la statistique | nouveau ; renvoi pour la veille sur les e-valeurs hors des agents (N-064) |
| Conjonction non trouvée | non trouvée, maintenu, à la profondeur de la section 1 | inchangé ; le verdict **occupée en partie** n'est pas modifié par cette lecture |

## 8. Nœuds pour Lazar (décisions à prendre, pas des conclusions)

1. **EvoSCM dans la note d'englobement.** La section 0, point 5, de la note d'englobement v3 ne donne l'engagement avant observation qu'à Ma et al. et la partie en temps réel à Koijen et Levy. Cette lecture trouve chez EvoSCM, pour des hypothèses proposées par un modèle de langue : un engagement avant l'existence des données (simulation à la demande), imposé par l'ordre du programme, sans scellement ; et une statistique (le postérieur) calculée par le programme. Décision : ajouter EvoSCM comme voisin de (i) + (iv-a, sans scellement) + (iv-b), et accepter ou non le statut **pris** pour (iv-b) au sens étroit (statistique hors des agents, qui n'est pas une règle de promotion). Option prudente (R4) : l'ajouter.
2. **Règle de retrait d'EvoSCM et (iii).** Évidence relative cumulée contre la meilleure concurrente, seuil -3,0 sur au moins trois plans, appliquée par le programme : la porter comme voisin de (iii) (règle séquentielle à seuil, sans e-valeur ni garantie, qui décide d'un retrait et non d'une promotion), ou ne pas la porter.
3. **Bancs non vérifiables sur code.** Le code des bancs de matériaux et de gènes (seuil 0,20, gel du graphe, prédictions stockées) n'est pas dans le dépôt public au commit lu. Décision : citer ces points comme lus sur le PDF seulement, ou faire rédiger une demande aux auteurs (rédigée ici sur demande, envoyée par Lazar).
4. **Information hors O4.** Le programme d'EvoSCM ajuste lui-même des familles de lois nommées dont deux correspondent à des mondes publics du banc ; le PDF dit qu'aucune équation de vérité n'est utilisée. Si EvoSCM est cité comme base de comparaison ou comme résultat, décider s'il faut mentionner cette réserve (R4).
5. **Classement EvoSCM et WAHL** (laissé ouvert par la v2) : toujours ouvert ; cette lecture ajoute à EvoSCM (iv-b) au sens étroit et précise (iv-a).

## 9. Ce qui reste non lu

- Code des bancs de matériaux (LLEMA) et de gènes (ActiveSciBench-GRN) : absent du clone ; non cherché ailleurs (consigne : rien au réseau).
- Dans le clone : les parties de scm_pipeline.py parcourues seulement (section 1.2), evaluator.py, executor.py, worlds.py, mse_fitting.py, load_trajectories.py, PhysicsSchool/physchool/*, les invites d'instructions autres que le gabarit, la plupart des essais, transfer.py l. 140-179, README.md hors l. 20-110, les images.
- Page du projet (adresse donnée p. 1), version v1 d'arXiv : non lues.
- Les tracés des figures 1, 3, 5, 6, 7, 8 (seul leur texte extrait est lu).

## 10. Incidents et refus, tels quels

- Aucun refus de permission, de crochet ou de classifieur rencontré pendant la lecture et la rédaction.
- Premier rejeu des extraits de code : 41 sur 42 ; échec sur scm_protocol.md (plage l. 174-176 dite, alors que le début de l'extrait est en l. 173). Corrigé **sur la source** (plage 173-176), programme inchangé ; les deux fichiers JSON de cet essai, créés par moi et non versés, ont été effacés puis réécrits ; second rejeu : 42 sur 42, code de sortie 0.
- Écart à la consigne : la consigne demande de lire tout le code Python ; une partie est seulement parcourue (section 1.2), déclarée ici.
- Les fichiers de configuration et le lisez-moi du clone nomment un modèle de langue commercial comme juge des explications ; son nom n'est pas recopié ici (consigne). .env.example lu par ses noms de variables seulement ; aucune valeur de clé lue ni affichée.
