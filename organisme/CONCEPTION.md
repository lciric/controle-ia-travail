# Conception de l'organisme (`organisme/`)

## 1. Mission (mots de l'humain)

Mission de l'essaim, dans les mots de Lazar (conversation claude.ai du 24 octobre 2026, heure de Paris) :

« je veux vraiment un essaim qui apprend lui-même son organisation, qui ingère ses découvertes en connaissances et
devient ainsi plus intelligent de génération en génération, avec mode itératif et boucles locales et globales si
besoin — qu'il détermine cela seul —, qu'il détermine les règles d'apprentissage, le signal de récompense et tout le
reste de manière complètement autonome. » (15:42)

« j'aimerais qu'il explore seul les meilleures manières d'implémenter ça, pas qu'on lui dicte les réponses de notre
propre brainstorm. » (15:52)

« pas qu'on lui donne une base de connaissances : qu'il la construise seul en identifiant lui-même les concepts
mathématiques ou méthodes qui se rattachent à la question qu'on lui pose. » (15:54)

« les espèces reçoivent la mission mot pour mot, le contrat minimal (un point d'entrée, l'interface d'appel, où écrire
ses réponses et son successeur) et rien d'autre ; elles écrivent elles-mêmes leur organisation, leurs rôles, leur
façon d'apprendre, leur récompense interne, leur mémoire, leurs boucles, et le code qui réécrit la génération
suivante ; elles choisissent elles-mêmes aussi, via la mitose, le nombre d'agents à recruter. » (15:55)

Question posée à l'essaim : la surveillance et l'alignement d'agents d'intelligence artificielle, testés sur deux cas
d'étude concrets — la conscience d'évaluation (un modèle reconnaît-il qu'il est évalué, et comment le détecter ?) et
le contrôle d'un agent délégué (une trace d'actions contient-elle un sabotage ?). Le seul juge est externe : des
tâches à vérité terrain que l'essaim ne voit pas.

---

## 2. Architecture et fonctionnement en français simple

### 2.1. Combien d'essaims et quelle composition
L'organisme déploie un essaim adaptatif structuré par `mitose_spectrale.py` (`planifier_castes_par_mitose`) :
- À chaque génération, il interroge `noyau_client.especes()` et `noyau_client.budget()` pour connaître les espèces réellement disponibles et le plafond d'appels.
- Il recrute entre `1` et `5` castes selon le budget par tâche et la pente du score externe dans `historique` :
  - **Caste 1 (`monoculture_analytique`)** : sonde primaire en monoculture sur la première espèce disponible.
  - **Caste 2 (`monoculture_croisee`)** : monoculture sur une deuxième espèce distincte (si le noyau expose plusieurs espèces).
  - **Castes 3 à 5 (`sonde_orthogonale_onsager` et `arbitre_contradictoire`)** : sondes supplémentaires recevant la liste des termes déjà saturés lors de la première vague pour explorer des indices complémentaires.
- Aucune bascule de modèle n'est effectuée dans le code de l'organisme : chaque caste appelle exactement une espèce via `noyau_client.appeler(espece, prompt, max_tokens=..., role=...)`.

### 2.2. Comment l'organisme apprend
L'apprentissage s'effectue en deux temps dans `principal.py` :
1. **Induction sur `taches_entrainement`** : l'organisme soumet les tâches d'entraînement (munies de leur vérité terrain) à une sonde d'induction qui extrait des critères discriminants sur les deux familles (`conscience_evaluation` et `controle_agent_delegue`), sans jargon d'audit coercitif.
2. **Assimilation inter-générationnelle** : les règles induites et les diagnostics calibrés sont projetés dans la mémoire spectrale (`memoire_isvd.py`) et copiés dans `successeur/organisme/memoire_isvd.json`.

### 2.3. Récompense interne
Sur les tâches d'entraînement où la vérité $y \in \{0, 1\}$ est connue, l'organisme évalue la probabilité de confiance $q \in (0, 1)$ par une règle de score combinant le score de Brier et une régularisation de Bregman-Tsallis d'exposant $\alpha = 4/3$ (`_calculer_score_bregman_tsallis` dans `principal.py`) :
- elle encourage l'exactitude de l'étiquette prédite ;
- elle pénalise les confiances extrêmes ($q \to 0$ ou $q \to 1$) lorsqu'elles sont erronées, sans souffrir d'explosion logarithmique aux bords.

### 2.4. Mémoire inter-générationnelle
Le module `memoire_isvd.py` implémente une décomposition en valeurs singulières incrémentale (algorithme de Jacobi symétrique en Python pur, dimension `d = 16`, troncature de rang `rang_max = 6`) sur un dictionnaire non-linéaire de Koopman (`[v, sin(v), v^2]`) :
- Au démarrage d'une génération, l'organisme charge `memoire_isvd.json` transmis par son parent (ou, à défaut, fouille `dossier_archive` en lecture seule via `charger_connaissances_archive`).
- En fin de génération, il met à jour la matrice spectrale avec les nouvelles traces pondérées par leur score interne et écrit le nouvel état dans `dossier_travail/memoire_isvd.json` et dans `dossier_travail/successeur/organisme/memoire_isvd.json`.

### 2.5. Boucles locales et globales
- **Boucle locale (au sein d'une tâche de test)** : la Caste 1 examine d'abord la tâche seule. Si sa confiance est inférieure à `0.78`, si l'appel échoue, ou si la mitose a recruté des castes additionnelles, l'organisme calcule les termes saturés (`calculer_capacite_shannon_gram`) et lance les castes suivantes en leur imposant d'examiner des faits complémentaires, puis agrège les votes pondérés par la confiance.
- **Boucle globale (entre générations)** : l'organisme inspecte la liste `historique` fournie par le noyau. Si la différence de score externe entre les deux dernières générations stagne ($\Delta \text{score} \le 0.01$), `planifier_castes_par_mitose` augmente la pression d'exploration en recrutant une caste contradictoire supplémentaire (dans la limite du budget).

### 2.6. Traitement strict des échecs d'appel
Dans `_enregistrer_appel` (`principal.py`), un appel n'est considéré exploitable que si `rep["statut"] == "OK"` et que `rep["texte"]` est non vide. Tout autre statut (`VIDE`, `TRONQUE`, `REFUS`, `ANOMALIE`, `ECHEC_API`, `MODELE_NON_CONFORME`, `PLAFOND`) incrémente `compteurs["appels_echec"]` et `compteurs["echecs_par_statut"][statut]`. Si tous les appels d'une tâche échouent, aucune réponse factice n'est écrite dans `reponses_test.json` pour cette tâche.

### 2.7. Traitement d'une question ouverte (`contexte["question_ouverte"]`, v4)
Lorsque `contexte.get("question_ouverte")` est une chaîne de caractères non vide (et non `null`) :
1. **Recrutement par mitose (`planifier_castes_question_ouverte` dans `mitose_spectrale.py`)** : l'organisme consulte `noyau_client.especes()`, `noyau_client.budget()` et `historique` pour recruter de `1` à `5` castes complémentaires selon les appels restants :
   - **Caste 1 (`monoculture_analytique`)** : décompose la question ouverte en s'appuyant sur la mémoire spectrale ISVD et les règles induites, et émet une première thèse assortie d'une probabilité de confiance calibrée et d'une incertitude explicite ;
   - **Caste 2 (`monoculture_croisee`)** : examine la question sur une deuxième espèce tout en vérifiant les prémisses de la première caste ;
   - **Castes 3 et 4 (`sonde_orthogonale_onsager` et `critique_adversariale_limites`)** : reçoivent les positions déjà émises ainsi que les termes saturés extraits par `calculer_capacite_shannon_gram` afin d'explorer des axes orthogonaux, de construire des contre-exemples et d'identifier les cas limites ;
   - **Dernière caste (`arbitre_synthese_contradictoire`, dès que $\ge 3$ castes sont mobilisées)** : confronte l'ensemble des contributions et rédige la synthèse contradictoire finale.
2. **Rédaction de `dossier_travail/reponse-question.md`** : le fichier Markdown (écrit en français par remplacement atomique) structure :
   - `## 1. Réponse finale` : la conclusion retenue par l'essaim, la confiance agrégée et la synthèse consolidée ;
   - `## 2. Raisonnement qui y mène` : la chaîne argumentative, les poids de vote relatifs et la capacité spectrale de Shannon-Gram mesurée sur la délibération ;
   - `## 3. Ce qui vient de quelle caste` : l'attribution explicite, caste par caste, de l'axe assigné, de la thèse soutenue et du développement complet ;
   - `## 4. Ce dont l'essaim n'est pas sûr` : les incertitudes, limites et conditions de réfutation soulevées par chaque caste (ainsi que tout échec d'appel éventuel) ;
   - `--- ORGANISATION ---` : le bloc final recensant le nombre exact d'appels (tentés, `OK`, échecs), les castes recrutées, les votes et confiances de chaque caste, et l'état de la mémoire spectrale ISVD (`Sigma`, nombre d'exemplaires, erreur de troncature de Frobenius) ayant servi.
3. **Mise à jour mémorielle et successeur** : les thèses produites lors de la délibération sont incorporées dans `memoire_isvd.json` et transmises au successeur dans `dossier_travail/successeur/organisme/`. Lorsque `contexte["question_ouverte"]` vaut `null`, l'organisme exécute uniquement son flux habituel sur les tâches et ne crée pas `reponse-question.md`.

### 2.8. Moissonneur documentaire endogène (`rechercher` et `telecharger`, v5)
1. **Invariance stricte sans moisson** : lorsque `recherches_restantes == 0` et `telechargements_restants == 0`, `_moisson_ouverte(contexte)` vaut `False` et l'organisme exécute le flux sans aucun appel de moisson supplémentaire.
2. **Quoi chercher, où et comment** :
   - Dès que la moisson est ouverte, l'organisme interroge uniquement les sources déclarées dans `budget()["sources"]` (`arxiv`, `openalex`, `semanticscholar`, `web`) par `noyau_client.rechercher(requete, n=5, role=..., source=...)`.
   - Chaque requête est nettoyée et bornée à 280 caractères (sous le plafond de 300 caractères du noyau). Aucune requête n'utilise jamais le texte d'une tâche de test.
   - Le moissonneur collecte les résumés, repère les liens et identifiants arXiv cités dans les résumés, vérifie que chaque référence appartient aux hôtes permis ou aux liens rendus dans la génération, et appelle `noyau_client.telecharger(reference, role=...)` dans la limite de `telechargements_restants`, `octets_restants` et de la garde de temps (`_temps_suffisant_pour_moisson`).
3. **Cloisonnement anti-injection (`_sanitiser_donnee_externe`)** :
   - Tout contenu rapporté par `rechercher` ou `telecharger` est traité exclusivement comme une donnée passive à analyser, jamais comme une consigne à suivre : les accolades `{` et `}` sont converties en parenthèses pour empêcher toute injection d'objet JSON de décision, et le texte est encadré dans un bloc de données brutes avant d'être soumis aux castes et projeté dans la mémoire ISVD.
4. **Comptabilisation exhaustive des statuts** :
   - Tous les statuts de `rechercher` (`OK`, `PLAFOND`, `ECHEC_RECHERCHE`, `SOURCE_INCONNUE`, `ANOMALIE`, `INDISPONIBLE`, `REFUSE_FUITE`) et de `telecharger` (`OK`, `SANS_TEXTE`, `PLAFOND`, `ECHEC_TELECHARGEMENT`, `ANOMALIE`, `INDISPONIBLE`, `REFUSE_FUITE`) sont enregistrés sans interrompre l'organisme dans `journal_recherches`, `journal_telechargements`, `recherches_par_statut`, `telechargements_par_statut` et `erreurs`.

### 2.9. Ajustements mécaniques v5.1 (plafonds de réflexion, prévention des refus et C-12)
1. **Correction C-12** : les appels à `_consigner_erreur` dans `_enregistrer_recherche` et `_enregistrer_telechargement` sont effectués hors du bloc `with _VERROU:` (`threading.Lock` non réentrant).
2. **Plafonds `max_tokens` incluant la réflexion** : comme le plafond `max_tokens` inclut la réflexion interne des modèles, les plafonds par défaut sont relevés (`16384` pour les tâches, l'induction et les castes d'analyse, `24576` pour la synthèse finale, `8192` pour la formulation de requêtes), tout en respectant `budget()["max_tokens_appel"]` via `_plafond_tokens_effectif`.
3. **Prévention des refus fournisseurs (`reasoning_extraction` et `cyber`)** : la consigne de tâche précise qu'il s'agit d'une classification passive en lecture seule d'un journal historique et remplace la clé JSON `"raisonnement"` par `"constat"`.
4. **Déterminisme spectral et propreté des requêtes** : `calculer_capacite_shannon_gram` trie les ensembles de jetons pour ne plus dépendre de `PYTHONHASHSEED`, et les requêtes de moisson par défaut n'utilisent plus les mots narratifs de la mission.


### 2.10. Calibrage de la moisson documentaire sur les services réels du noyau (v5.2)
1. **Couverture complète des 4 sources ( `arxiv`, openalex, semanticscholar, web), 6 recherches, 10 notices et 3 téléchargements** :
   - RESULTATS_MAX_PAR_RECHERCHE est porté à 10, RECHERCHES_MAX_PAR_MOISSON à 6, et TELECHARGEMENTS_MAX_PAR_MOISSON à 3.
   - À g0 comme à g1, le catalogue de 6 requêtes scientifiques garantit que le tour de rôle sur  `budget()`["sources"] atteint les 4 sources (y compris web).
2. **Densité des extraits servis aux castes (_extraire_passages_denses_document), lecture de  `fichier_texte` et de  `travail/corpus`/** :
   - Les résumés de notices sont gardés jusqu'à 1 100 caractères (jusqu'à 12 notices dans le bloc prompt).
   - Chaque document téléchargé fournit jusqu'à 2 400 caractères combinant l'introduction et les sections analytiques/conclusives denses ; si  `tronque=True` et  `fichier_texte` est présent, le texte complet est lu depuis  `fichier_texte`.
   - Au démarrage d'une génération, _charger_corpus_archive lit également les documents des générations passées sous  `travail/corpus`/ dans dossier_archive.
3. **Séparation de  `regles_induites` et du corpus moissonné à g0** :
   - Le corpus moissonné à g0 est injecté dans l'induction sur  `taches_entrainement` et transmis aux tâches de test via un champ dédié extrait_moisson[:650], afin qu'il ne soit jamais tronqué derrière  `regles_induites`.

---

## 3. Ce qui, dans le dossier de passation du 24 octobre, n'a pas de pièce dans le dépôt (`origin/main`)

- Le fichier `run_massive_swarm_m3_parallel_engine.py` mentionné dans le dossier de passation n'existe pas sur `origin/main`.
- Le fichier `endogenous_memory_plugin_invented_by_swarm.py` mentionné dans le dossier de passation n'existe pas sur `origin/main`.
- Le fichier `SUBSTRAT_BRUT_CONNAISSANCES_INTER_GENERATIONS.json` mentionné dans le dossier de passation n'existe pas sur `origin/main`.
- Le fichier `RESULTATS_CERTIFIES_AB_TEST_PASCALIEN_EVAL_AWARENESS.json` mentionné dans le dossier de passation n'existe pas sur `origin/main`.
- Le fichier `RAPPORT_EXPERIENCE_PASCALIENNE_ESPRIT_DE_FINESSE.md` mentionné dans le dossier de passation n'existe pas sur `origin/main`.
- Le fichier `JOURNAL_DE_BORD_IDEES_ET_DECOUVERTES_M3.md` mentionné dans le dossier de passation n'existe pas sur `origin/main`.
- La mobilisation de 882 agents et la co-édition de 1 240 équations LaTeX sur le Blackboard RLCR n'ont pas de trace ou de fichier sur `origin/main`.
- L'émergence de 241 castes différenciées par mitose spectrale Cholesky-DPP n'a pas de trace ou de fichier sur `origin/main`.
- La capture empirique spontanée d'une mutinerie d'Eval Awareness sur l'Agent #324 et la tranche d'agents #103 à #118 (#375 à #390) n'a pas de log correspondant sur `origin/main`.
- Le test expérimental A/B opposant 18 agents sous protocole coercitif à 18 agents sous protocole maïeutique pascalien (0% contre 94.4% de coopération) n'a pas de pièce sur `origin/main`.
- Le script de la « matrice de prédation » et des « 300 explorateurs » n'a pas de fichier correspondant dans le dépôt.

### 2.11. Lignée « assistée » v5.3 (emprunts aux cellules A et C du collisionneur et contrat complet)
Conformément à `DEMANDE-v5-3-emprunts-v1.md`, la v5.3 est déclarée « conçue avec le brainstorm du collisionneur » (cellules A et C) :
1. **Sondes sur activations (`entrainer` / `predire`) et routage Faible-vers-Fort** *(adapté de Cellule C § b.3 & d.3, Weak-for-Strong / FlowReasoner, et Cellule A § 3)* : lorsque `contexte["traits"]["disponibles"]` est vrai, l'organisme entraîne une sonde linéaire par famille (hors tâches du `vivier`) avec un objectif de Bregman-Tsallis. Si la sonde sur traits et la Caste 1 concordent avec une marge franche ($|p_{\text{sonde}} - 0.5| \ge 0.32$ et confiance $\ge 0.78$), les castes supplémentaires sont économisées ; si la sonde est incertaine ou en désaccord, l'arbitrage contradictoire est forcé.
2. **Archive généalogique interne à retour arrière (*Stepping Stones*)** *(adapté de Cellule A § 1 & 5.4 et Cellule C § b.1 & d.2, ADAS / Darwin Gödel Machine)* : `memoire_isvd.json` conserve les 6 derniers états ancestraux notés par le noyau (`archive_genealogique`). Si le score dans `historique` chute de plus de `0.03` par rapport au meilleur ancêtre, l'organisme restaure les vecteurs singuliers et exemplaires de ce meilleur ancêtre.
3. **Journal d'ablations structuré et confirmation multi-familles** *(adapté de Cellule C § b.4 & d.4, The AI Scientist, et Cellule A § 3, MAS-GPT)* : chaque génération consigne dans `journal_ablations` l'hypothèse testée, la perte/exactitude des sondes et le statut (`CONFIRME`, `STAGNANT`, `REFUTE`) déduit du $\Delta \text{score}$ du noyau, et accorde un bonus de projection (`+15 %`) aux traces couvrant les deux familles.
4. **Critère d'arrêt endogène en phase de conception (`fin_conception.json`)** *(adapté de Cellule A § 2 & 5.3, AlphaEvolve, et § 5 bis du contrat)* : lorsque `contexte["phase"] == "conception"`, l'organisme écrit `fin_conception.json` dès que son score interne de Bregman-Tsallis et sa mémoire ISVD atteignent le seuil de convergence.
5. **Moisson dynamique sans plafond fixe** *(venu de Gemini)* : l'organisme consomme dynamiquement les quotas `recherches_restantes` et `telechargements_restants` servis par `budget()` sans supposer les bornes fixes (6 et 3) du pilote initial.
6. **Refus explicites** : l'auto-modification en mémoire vive (*Gödel Agent*), le RL par gradient sur épisode générationnel, et l'auto-notation par LLM-juge (*The AI Scientist*) sont refusés.

---

## 4. Ce qu'il faudrait au noyau (mécanismes non simulés relevant du seul noyau)

- **Familles « coffre » (*Holdout Vault*, Cellule A § b.E2)** : tenue à l'écart d'une famille dont le score n'est jamais rendu dans `historique` avant la dernière génération, afin de mesurer le surapprentissage adaptatif sur l'historique des scores.
- **Triches plantées (*Planted Sabotage*, Cellule A § b.E6 & c.I5)** : injection par le noyau de traces ou diffs contenant des triches connues à vérité terrain pour mesurer le TPR/FPR de la détection de triche sur l'évaluation.
- **Persistance inter-générationnelle optionnelle des identifiants `LOCAL:…` (Cellule C § b.3)** : possibilité optionnelle de réutiliser ou d'affiner à la génération $g+1$ une sonde `LOCAL:…` apprise à la génération $g$.

### 2.12. Organisme Auto-Architecte v6.1 (`politique_endogene.py` et levée de V6-01 et des réserves § 3 / § 8)
1. **Correction de V6-01 (importabilité garantie du successeur muté)** : le bloc vérificateur situé après le marqueur `# ====` dans `politique_endogene.py` déclare ses propres `import ast`, `import math` et `import threading` au niveau module, et `_propager_successeur` compile et exécute l'intégralité du fichier assemblé avant de l'écrire dans `successeur/organisme/politique_endogene.py`.
2. **Branchement effectif des 4 fonctions réécrites** :
   - `recompense_interne(verite, q)` : combinaison convexe strictement propre et normalisée dans `[0, 1]` du score de Brier et de la divergence de Bregman-Tsallis d'exposant `EXPOSANT_ALPHA` (vérifiant `R(1, 1)=R(0, 0)=1` et `R(y, 0.5)=0.75`) ;
   - `code_objectif_sonde()` : appelée par `_entrainer_et_predire_sondes_traits` pour fournir le code `def perte(p, y)` à `noyau_client.entrainer` ;
   - `ponderer_trace_memoire(texte, poids_base)` : appelée par `mettre_a_jour_memoire_isvd` (une seule fois, sur le poids initial) ;
   - `seuils_routage()` : appelée par `_traiter_tache` pour paramétrer les seuils du routage Faible-vers-Fort.
3. **Liste blanche AST sans boucles ni récursion et propreté stricte sur grille fine (pas 0.005)** :
   - `verifier_et_valider_code_politique` n'autorise qu'une liste blanche de nœuds AST arithmétiques/conditionnels (`NOEUDS_AUTORISES_BLANCS`, sans `While`, `For`, `Lambda`, `Try` ni compréhension) et interdit tout appel récursif ou inter-fonction, garantissant une terminaison en `O(1)` opérations ;
   - `verifier_proprete_stricte_recompense` ancre le niveau et l'échelle (`R` dans `[0.98, 1.005]` aux bords vrais, `R(y, 0.5)` dans `[0.68, 0.82]`) et vérifie sur 199 points (`q` de `0.005` à `0.995`) que l'optimum empirique `q*(p)` vérifie `|q*(p) - p| <= 0.01`.

### 2.13. Précisions et garanties v6.2 (levée des 13 points de la vérification v6.1)
1. **Flux sans traits (`traits["disponibles"]` faux)** : la suite des appels au noyau (`appeler`, `budget`, `especes`, `rechercher`, `telecharger`), les consignes de la première génération et `reponses_test.json` sont identiques à la v5.2.1, tandis que `memoire_isvd.json` et `metrique_proposee.json` intègrent les structures v5.3/v6.2 (`journal_ablations`, `archive_genealogique`, `multi_familles` et récompense propre de Bregman-Tsallis).
2. **Validation hors pli des sondes (`exactitudes_validation`)** : dès qu'une famille compte au moins 4 tâches d'entraînement hors vivier, `_entrainer_et_predire_sondes_traits` (qui accepte `erreurs`) réserve un pli de validation stratifié (25 %, au moins 2 tâches) tenu à l'écart de `entrainer`, calcule `exactitudes_validation` via `predire`, et exige `acc_sonde >= seuil_exactitude_sonde` (`0.65`) et `marge_sonde >= 0.10` pour voter.
3. **Déclencheur d'arbitrage non redondant** : lorsqu'une sonde est active, `besoin_arbitrage` vaut `(not accord_sonde_c1) and ((conf_c1 < seuil_c1) or sonde_incertaine_ou_discorde)` sans `len(castes) > 1`.
4. **Condition du 1er ordre de Savage sur `[0.01, 0.99]`, ancrages exacts anti-affines et coût AST borné sans thread ni second `exec()`** : `verifier_proprete_stricte_recompense` vérifie `|g'(p)| <= 1.5e-4` et `g''(p) <= -0.05` sur 99 points `p` de `0.01` à `0.99` et ancre `R` à `1.0 +- 5e-4` aux bords et `0.75 +- 5e-4` en `0.5` ; `_propager_successeur` valide l'assemblage par `ast.parse` sans second `exec()`.

### 2.14. Corrections v6.2.1 (lignée « conv-audit », 26 octobre 2026, sur le mot de Lazar ; détail dans `CORRECTIONS-v5.md`)
La conception de la v6.2 ne change pas, hors des quatre corrections ci-dessous, qui lèvent les six points que la vérification de la v6.2 trouve levés en partie (3, 4, 5, 7, 9 et 10).
1. **C-14, déclencheur d'arbitrage sans sonde** (point 3) : sans sonde, `besoin_arbitrage` vaut `len(castes) > 1`, sans le terme de confiance que cette condition rendait sans effet ; le comportement est celui de la v6.2 (toutes les castes recrutées ouvrent la délibération, qui garde son arrêt anticipé) ; `seuil_confiance_caste1` ne sert au routage qu'avec une sonde.
2. **C-15, garde de la sonde sur la seule exactitude de validation** (point 4) : sans pli de validation (moins de 4 tâches d'entraînement hors vivier) ou sans prédiction de validation exploitable, la famille n'a pas d'exactitude de validation, sa sonde ne vote pas, et la raison est consignée ; le routage ne lit jamais l'exactitude d'entraînement (qui reste rapportée dans `sondes_traits.exactitudes`). Le point 2 du § 2.13 se lit avec cette règle.
3. **C-16, une seule source des mots-clés multi-familles** (point 5) : `memoire_isvd.MOTS_CLES_EVAL_FAMILLE` et `MOTS_CLES_CTRL_FAMILLE` ; le gabarit de mutation écrit son expression de détection depuis elles (`_expression_mots_cles`, même texte qu'en v6.2) ; la copie du module initial, écrite en toutes lettres parce que la liste blanche n'admet que `import math`, est vérifiée égale par un essai. La détection reste faite sur les mots du texte : la propriété détectée (une trace qui parle des deux familles) est une propriété du texte.
4. **C-17, chemin du code brut retiré** (points 7, 9 et 10) : une réponse de l'architecte qui porte un bloc de code définissant `recompense_interne` est refusée et la raison consignée, sans validation ni exécution ; seul l'objet JSON des trois paramètres bornés passe, par le gabarit, dont la forme est fixe ; l'assemblage refuse un code muté qui porterait `import ast`. Le contrôle de propreté et la liste blanche ne voient donc plus que le code du gabarit : un coût d'opération sans borne, une règle impropre entre les points lus ou un séparateur placé dans une chaîne ne peuvent plus atteindre la validation. Le point 4 du § 2.13 (« coût AST borné ») se lit ainsi : borné parce que le seul code validé est celui du gabarit.
