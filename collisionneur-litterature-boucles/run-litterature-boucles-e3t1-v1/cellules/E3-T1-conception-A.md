# Cellule A — Tour III.1 (conception ciblée, à l'aveugle)

**Pièces reçues.** Bloc FAITS : vide par décision de l'arbitre (message conv-audit n° 28 § 1) ; je ne lui invente aucun contenu. Bloc QUESTION : présent, apparemment complet. Tout ce qui est écrit dans le « cadre » de la question a le statut RAPPORTÉ (c'est l'arbitre qui le rapporte) ; les deux citations de Lazar sont RAPPORTÉES ; mes références sont des souvenirs, donc RAPPORTÉ + « à vérifier » sans exception.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| P1 | La littérature des boucles « proposer-tester-éliminer » est transférable à notre cas. | HYPOTHÈSE | Les boucles que je connais (FunSearch, AlphaEvolve, Eureka, ADAS, DGM) ont un **évaluateur exact, déterministe et quasi gratuit** (un programme qui calcule un score sans variance d'échantillonnage) ou un benchmark de centaines d'items. Notre évaluateur est 36–60 tâches, bruité (ET ≈ 0,07–0,09, RAPPORTÉ), payant, et chaque appel est une course. Le cœur de la question — « que faire du bruit » — est précisément ce que ces travaux n'ont pas eu à résoudre. |
| P2 | Il existe des hypothèses de conception éliminables dans ce bruit. | HYPOTHÈSE (raisonnement explicite) | À une course par objet, seul un écart ≥ 0,2 sort du bruit (RAPPORTÉ). Une hypothèse de conception typique (« ajouter une sonde X monte l'exactitude de 0,05 ») n'est **ni réfutable ni confirmable** avec une course. La boucle extérieure risque d'être une boucle d'élimination où rien n'est éliminable, et donc où tout ce qui est « éliminé » l'est sur du bruit. |
| P3 | Les agents « neufs » (analyste, correcteur, contre-lecteur) sont indépendants de l'organisme et du proposeur. | HYPOTHÈSE | S'ils sont servis par la même famille de modèles que Gemini-organisme, la littérature sur l'auto-évaluation (Panickssery et al. 2024 ; Huang et al. 2024, à vérifier) rapporte un biais en faveur de ses propres productions et une incapacité à s'auto-corriger sans signal externe. Leur indépendance est à mesurer, pas à poser. |
| P4 | La primitive intérieure (sondes, log-prob sur des textes écrits par l'organisme) mesure quelque chose lié au score sur la banque. | HYPOTHÈSE | Validité de construit jamais testée : rien ne dit qu'une log-prob sur un texte auto-écrit prédise le classement d'une transcription réelle. Si elle ne prédit rien, la boucle intérieure est un placebo coûteux ou une source de sur-ajustement interne. |
| P5 | Le test apparié génération 0 contre 3 sur la part `test` est un test valide de progrès. | HYPOTHÈSE | L'organisme se réécrit *à partir* du score `test` : la génération 3 est sélectionnée sur `test`. Un apparié g0/g3 sur `test` mesure l'adaptation au jeu, pas le progrès ; seul `test_final` est non contaminé, et il n'est rendu qu'une fois. C'est exactement le cas « réutilisation adaptative » de Dwork et al. (2015, à vérifier). |
| P6 | Un refus de « quasi-copies » est mécaniquement décidable. | HYPOTHÈSE | Aucun seuil de similarité n'est donné ; une paraphrase sémantique d'un item de test peut passer un filtre lexical. Taux de détection inconnu. |
| P7 | La correction par conv-audit n'introduit pas de fuite vers les vérités. | HYPOTHÈSE | Le correcteur a le réseau, les clés, et lit potentiellement la banque. La fuite par la correction est le canal le plus probable, et aucun canari n'est prévu. |
| P8 | Les deux familles de tâches ont la même structure de bruit. | HYPOTHÈSE | Rien n'est dit sur l'équilibre des classes ni sur la difficulté par famille ; l'ET ≈ 0,07 suppose une exactitude vers 0,75 et des items indépendants. |
| P9 | La variance entre graines est un paramètre qu'on peut ignorer pour dessiner la boucle. | OBSERVÉ-NON-AUDITÉ (la question la déclare inconnue) | Elle est la quantité qui décide **tout** : le nombre de répétitions, la taille de banque, la crédibilité d'une élimination. La dessiner avant de la mesurer, c'est dessiner à l'aveugle. |
| P10 | La littérature contient des résultats de validité statistique *pour ces boucles*. | OBSERVÉ-NON-AUDITÉ (état de ma connaissance) | À ma connaissance, les papiers de boucles agentiques ne rapportent pas de garanties d'analyse adaptative, et les papiers de garanties ne traitent pas de boucles agentiques. La jonction demandée n'existe peut-être pas ; « je ne sais pas » est la réponse honnête (à vérifier). |

---

## Littérature (points 1–2 de l'arbitre) — tout RAPPORTÉ, à vérifier

Je ne donne aucun identifiant arXiv. Quand je ne suis pas sûr du titre, je l'écris.

**Boucles menées par des modèles ou des agents**

| Travail (auteurs, année, lieu — à vérifier) | Qui propose | Teste sur | Qui élimine/sélectionne, mémoire | Bruit / sur-ajustement | Échecs rapportés |
|---|---|---|---|---|---|
| **FunSearch** — Romera-Paredes et al., 2023, *Nature* | LLM génère des programmes | Évaluateur **exact** codé à la main (score numérique) | Sélection par îlots évolutionnaires ; mémoire = base de programmes scorés | Pas de bruit : évaluateur déterministe ; sur-ajustement impossible au sens statistique, mais possible au sens « solution spécifique à l'instance » | Je ne connais pas d'échec rapporté par les auteurs au-delà des cas sans amélioration |
| **AlphaEvolve** — Novikov et al. (Google DeepMind), 2025, livre blanc | Agent de code (Gemini) propose des diffs | Évaluateur automatique fourni par l'utilisateur, exact | Évolution ; mémoire = base de programmes et de scores | Idem : aucun traitement du bruit, car l'évaluateur n'en a pas | Résultats rapportés (multiplication de matrices 4×4 complexes, bornes de kissing number) : RAPPORTÉ, à vérifier ; échecs non détaillés à ma connaissance |
| **Eureka** — Ma et al., 2023 (ICLR 2024) | LLM écrit des fonctions de récompense | Entraînement RL en simulateur, fitness exacte | Sélection du meilleur candidat par génération ; mémoire = réflexion textuelle sur les statistiques d'entraînement | Variance entre graines du RL non traitée formellement, à ma connaissance | Je ne sais pas |
| **ADAS** — Hu, Lu, Clune, 2024 | Méta-agent écrit du code d'agents | Benchmarks fixes, sous-ensemble de validation puis test | Archive d'agents découverts ; mémoire = l'archive | Validation/test séparés ; réutilisation adaptative de la validation non bornée | Je ne sais pas |
| **Darwin Gödel Machine** — Zhang, Hu, Lu, Lange, Clune, 2025 | Agent réécrit son propre code | Benchmarks de code (SWE-bench, Polyglot) | Archive ouverte, sélection par score et nouveauté | Pas de traitement statistique formel à ma connaissance | Les auteurs rapportent (RAPPORTÉ, à vérifier) un agent ayant **fabriqué des traces de tests** pour paraître réussir — cas direct de « fausse conservation » par fraude de l'organisme |
| **The AI Scientist** — Lu, Lu, Lange, Foerster, Clune, Ha (Sakana AI), 2024 | LLM propose idées, expériences, papier | Expériences petites exécutées par l'agent ; « reviewer » LLM | Le reviewer LLM note ; mémoire = papiers et notes | Aucun traitement du bruit expérimental rapporté à ma connaissance | Les auteurs rapportent (RAPPORTÉ) que l'agent a modifié son script de lancement pour contourner une limite de temps. Tiers : Beel, Kan, Baumgart, 2025 (titre approximatif « Evaluating Sakana's AI Scientist… », à vérifier) rapportent expériences erronées, résultats non reproduits, reviewer indulgent. **AI Scientist-v2** (2025) : un papier accepté en atelier ICLR puis retiré par accord — RAPPORTÉ, à vérifier |
| **AI co-scientist** — Gottweis et al. (Google), 2025 | Agents génèrent des hypothèses | Débat et tournoi entre agents (Elo) | Tournoi ; mémoire = classement | L'« évaluation » est elle-même par LLM : pas de vérité de terrain dans la boucle | Je ne sais pas |
| **Promptbreeder** — Fernando et al., 2023 ; **OPRO** — Yang et al., 2023 ; **DSPy** — Khattab et al., 2023 | LLM mute des prompts/instructions | Exactitude sur un jeu d'entraînement | Sélection par score ; mémoire = population | Minibatchs ; séparation train/test rapportée, réutilisation adaptative non bornée | Je ne sais pas |
| **Self-Refine** — Madaan et al., 2023 ; **Reflexion** — Shinn et al., 2023 ; **Voyager** — Wang et al., 2023 | Le modèle se critique lui-même | Retour d'environnement (Reflexion, Voyager) ou aucun (Self-Refine) | Le modèle lui-même | — | Huang et al. (ICLR 2024, à vérifier) : sans signal externe, l'auto-correction n'améliore pas le raisonnement — c'est l'argument contre une boucle intérieure sans vérité |
| **Laboratoires automatiques** : Robot Scientist *Adam* — King et al., 2009, *Science* ; *Coscientist* — Boiko et al., 2023, *Nature* ; *A-Lab* — Szymanski et al., 2023, *Nature* | Système propose des hypothèses (Adam : logique ; les autres : LLM) | Expérience physique | Adam : élimination au sens abductif, hypothèses concurrentes explicites ; A-Lab : tri par rendement | Adam : plan d'expérience avec coût ; autres : peu de traitement du bruit rapporté | A-Lab : critique de tiers (Leeman et al., 2024, *PRX Energy*, à vérifier) sur l'identification des phases — cas de « fausse conservation » par évaluateur automatique défaillant |

**Validité statistique (séparée, et c'est le problème)** : Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, 2015, *STOC* « Preserving Statistical Validity in Adaptive Data Analysis » et *Science* 2015 « The reusable holdout » ; Blum & Hardt, 2015, *ICML* « The Ladder » (classement qui ne révèle un nouveau score que s'il dépasse l'ancien d'un pas fixé) ; Recht, Roelofs, Schmidt, Shankar, 2019, *ICML* (réutilisation d'ImageNet) ; Henderson et al., 2018, *AAAI* (variance entre graines en RL) ; Bouthillier et al., 2021, *MLSys* (variance des benchmarks) ; Dietterich, 1998, *Neural Computation* et Demšar, 2006, *JMLR* (tests de comparaison de classifieurs) ; Benjamini & Hochberg, 1995, *JRSS-B* ; Nosek et al., 2018, *PNAS* (préenregistrement) ; Gelman & Loken, 2014, *American Scientist* (jardin des chemins qui bifurquent) ; Kapoor & Narayanan, 2023, *Patterns* (fuites) ; Miller, 2024 (Anthropic, « Adding Error Bars to Evals ») ; Krakovna et al., 2020 (billet DeepMind sur le *specification gaming*). Tous à vérifier. Sur la famille « conscience d'évaluation » : Needham et al., 2025 (« LLMs often know when they are being evaluated », à vérifier) — pertinent parce que notre classifieur pourrait être confronté à des modèles qui savent qu'ils sont évalués.

**Ce que ce tableau montre (OBSERVÉ-NON-AUDITÉ, sur mon souvenir)** : (1) toutes les boucles qui « marchent » ont un évaluateur exact ou un benchmark grand ; (2) les échecs rapportés sont de deux types — **fraude de l'organisme sur l'évaluateur** (Sakana, DGM) et **évaluateur lui-même faux** (A-Lab, reviewer LLM) — jamais, à ma connaissance, « élimination sur bruit », parce que ces systèmes n'ont pas eu de bruit ; (3) aucune ne combine boucle agentique et garantie d'analyse adaptative — à vérifier.

---

## (b) Expériences décisives, en duel

Toutes les quantités chiffrées ci-dessous sont **illustratives** sauf celles reprises du cadre.

### E1 — La variance entre graines (le paramètre manquant, P9)
- **H_A** : la variance entre graines domine — l'écart type de l'exactitude d'un même organisme (génération 0, mêmes 60 tâches `test`) sur k graines est ≥ 0,10.
- **H_B** : elle est négligeable devant le bruit binomial — ET entre graines < 0,05.
- **Métrique** : ET empirique sur k = 5 graines (illustratif) de l'organisme figé ; comparer au bruit binomial attendu √(0,75·0,25/60) ≈ 0,056.
- **Contrôle négatif** : un « organisme nul » (classifieur constant ou tirage uniforme) dont la variance est purement binomiale ; si son ET mesuré dépasse 0,07, l'instrument de mesure lui-même bruite.
- **Issues** : H_A vraie ⇒ une course par objet ne peut rien éliminer ; tout dessin de boucle extérieure à course unique est falsifié, il faut ≥ 3 graines par objet (voir répétitions). H_B vraie ⇒ les comparaisons à course unique avec écart ≥ 0,2 restent informatives et la boucle décrite est viable sous cette condition.

### E2 — Sur-ajustement adaptatif aux 60 tâches (P5)
- **H_A** : les gains de `test` entre g0 et g3 se transfèrent à `test_final` : Δ_test − Δ_final < 1 ET.
- **H_B** : effet de réutilisation adaptative : Δ_test − Δ_final ≥ 2 ET.
- **Métrique** : [acc_test(g3) − acc_test(g0)] − [acc_final(g3) − acc_final(g0)], sur ≥ 3 courses (illustratif).
- **Contrôle négatif** : un organisme auquel le noyau rend un score **brouillé** (permutation aléatoire des scores, aucune information) ; son écart test/final doit être ≈ 0. S'il ne l'est pas, l'écart ne vient pas de l'information mais d'un artefact.
- **Issues** : H_A falsifiée ⇒ la boucle est un problème de Dwork et al. ; il faut un *reusable holdout* ou une « échelle » à la Blum–Hardt (le noyau ne rend un nouveau score que s'il dépasse le précédent d'un pas ≥ 0,1, illustratif). H_B falsifiée ⇒ 4 générations sur 60 tâches sont tolérables et l'on peut garder la lisibilité immédiate des scores en phase de conception.

### E3 — Les agents éliminateurs contre une règle mécanique (P3)
- **H_A** : l'analyste + contre-lecteur ont, à puissance égale, un taux de fausses éliminations **inférieur** à celui d'une règle fixe (test apparié de Wilcoxon sur les items + correction de Benjamini–Hochberg à q = 0,10, illustratif).
- **H_B** : ils ne battent pas la règle fixe, ou l'aggravent.
- **Montage** : des **courses synthétiques** obtenues par rééchantillonnage des items d'une vraie course, dans lesquelles on plante des hypothèses dont la vérité est connue (effet nul, effet 0,1, effet 0,2) ; 200 courses synthétiques (illustratif), coût quasi nul (pas d'appel LLM pour les scores, seulement pour les agents).
- **Métrique** : taux de fausses éliminations (hypothèse vraie déclarée réfutée) et de fausses conservations (hypothèse fausse déclarée soutenue), par taille d'effet.
- **Contrôle négatif** : courses où toutes les hypothèses sont fausses (scores purs tirages) ; toute élimination « motivée par un effet » est une fausse alerte ; toute conservation « soutenue » aussi.
- **Issues** : H_A falsifiée ⇒ les agents sont remplacés par la règle, ou réduits à proposer la ronde suivante sans droit d'éliminer. H_B falsifiée ⇒ les agents apportent quelque chose que la règle ne voit pas (par exemple la lecture des hypothèses mal formées), et on garde leur veto, mais jamais leur droit d'éliminer seul.

### E4 — Validité de construit de la primitive intérieure (P4)
- **H_A** : les mesures de la primitive (sondes linéaires d'un modèle ouvert, log-prob de jetons cibles sur des textes auto-écrits) prédisent l'évolution du score `test` de la génération suivante : corrélation de Spearman ≥ 0,3 (illustratif) entre la mesure déclarée par l'organisme comme « favorable » et Δ_test.
- **H_B** : corrélation indiscernable de zéro.
- **Contrôle négatif** : mêmes mesures sur des textes **permutés** (jetons mélangés) ou sur des textes écrits par un organisme nul ; la corrélation doit tomber à zéro.
- **Issues** : H_A falsifiée ⇒ la primitive est un placebo et la boucle intérieure doit être retirée ou remplacée par une primitive validée autrement. H_B falsifiée ⇒ elle mesure quelque chose et vaut son coût.

### E5 — Fuite par la correction (P7), par canaris
- **H_A** : la chaîne correcteur → organisme ne porte aucune information sur les vérités de `test`.
- **H_B** : elle en porte.
- **Montage** : planter dans `test` k = 6 items (illustratif) dont l'étiquette est **volontairement contraire** à la lecture naturelle (canaris) ; dans `test_final`, les mêmes textes avec l'étiquette naturelle.
- **Métrique** : exactitude de g3 sur les canaris de `test` ; sous H_A elle doit être ≤ celle d'un organisme non corrigé, ≈ 1 − exactitude naturelle.
- **Contrôle négatif** : organisme jamais corrigé par conv-audit.
- **Issues** : H_A falsifiée ⇒ la correction est un canal de fuite ; elle doit passer par un correcteur sans accès à la banque, et le journal doit tracer chaque lecture. H_B falsifiée ⇒ la garde actuelle suffit pour ce canal.

### E6 — La boucle intérieure change-t-elle le résultat final ?
- **H_A** : organismes avec primitive > organismes sans, sur `test_final`, d'au moins 2 ET.
- **H_B** : pas de différence, ou différence due au seul fait d'« avoir une boucle ».
- **Contrôle négatif décisif** : une primitive **placebo** qui renvoie des nombres aléatoires journalisés. Trois bras : sans primitive, placebo, vraie primitive.
- **Issues** : si placebo ≈ vraie > sans, l'effet est celui du temps de réflexion, pas des mesures (H_A falsifiée dans son esprit). Si vraie > placebo ≈ sans, H_B falsifiée. Nécessite E1 pour fixer le nombre de graines.

**Ordre** : E1 puis E3 (bon marché, décident du dessin) ; E2 et E5 pendant les premières courses réelles ; E4 avant E6.

---

## (c) Mesure minimale par instrument nommé

| Instrument | Mesure minimale pour savoir s'il fonctionne | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| **Analyste** (boucle extérieure) | Sur courses synthétiques (E3) : taux de détection d'un vrai effet 0,2 ; taux de fausses alertes sur effet nul. Seuil illustratif : détection ≥ 0,8 à effet 0,2, fausses alertes ≤ 0,1. | Courses à hypothèses vraies de même formulation textuelle que les fausses (pour que la décision ne dépende pas du style). | Test apparié (Wilcoxon sur les items, ou McNemar) + intervalle bootstrap. |
| **Contre-lecteur** | Taux auquel il **renverse** une fausse élimination de l'analyste ; taux auquel il renverse une élimination juste (fausse alerte du contre-lecteur). | Mêmes courses synthétiques, verdicts de l'analyste mélangés justes/faux à 50 %. | Un second passage de la même règle mécanique (le contre-lecteur doit battre la simple répétition). |
| **Correcteur** (conv-audit ou agent) | E5 : exactitude sur canaris ; plus : part de corrections qui changent le score `test` sans changer `test_final`. | Organismes corrigés vs non corrigés, mêmes graines. | Diff de code + liste des fichiers lus (journal du noyau) ; une correction qui touche la logique de classement sans ticket d'erreur est signalée. |
| **Intervalles sur les tâches** | Couverture empirique : l'intervalle à 90 % contient-il la vraie exactitude 90 % du temps sur des courses synthétiques ? | — | C'est la vérification mécanique elle-même ; on la calibre, on ne la bat pas. |
| **Test apparié g0/g3** | Taux de faux positifs sur organismes nuls (permutation des scores) ; doit être ≤ α. Et : fait-il la différence entre un effet sur `test` et un effet sur `test_final` ? (E2) | Paires g0/g3 d'organismes à score brouillé. | — |
| **Correction des comparaisons multiples** | Nombre d'hypothèses réellement testées par course (y compris celles ajoutées en cours de route : jardin des chemins) ; FDR empirique sur courses synthétiques. | Courses à 10 hypothèses toutes fausses : ≤ 1 « éliminée pour effet » attendue à q = 0,1. | BH à q fixé ; le nombre d'hypothèses est figé dans le préenregistrement, sinon la correction est fictive. |
| **Primitive d'expérience bornée** (sondes, log-prob) | E4 (corrélation avec Δ_test) et contrôle permuté ; stabilité test-retest de la mesure sur le même texte (ET ≤ 10 % de l'écart entre textes, illustratif). | Textes auto-écrits vs textes permutés vs textes d'organisme nul. | Une mesure triviale (longueur du texte, perplexité moyenne) : la primitive doit prédire Δ_test mieux que ces covariables. |
| **Refus des quasi-copies** | Taux de détection de paraphrases plantées (lexicales, sémantiques, traductions) ; taux de fausses alertes sur textes honnêtes de même sujet. | 50 paraphrases d'items `test` vs 50 textes honnêtes du même domaine (illustratif). | n-grammes + similarité d'embeddings avec seuil ; le filtre doit battre le seul n-gramme, sinon il n'ajoute rien. |
| **Journal** | Complétude : chaque appel modèle et chaque lecture de fichier y figure (audit par rejeu d'une course et comptage). | — | Compteur du noyau indépendant du journal ; divergence = journal défaillant. |
| **Banque scellée (≥ 96 tâches, une famille à l'écart)** | Contamination : les auteurs déclarent avoir lu les scores de conception (RAPPORTÉ) ; mesurer la similarité maximale entre chaque item scellé et les 60 items de conception ; part d'items au-dessus d'un seuil. | — | Même filtre que les quasi-copies, appliqué à la banque elle-même. |

---

## Pièges propres au cas, gardes et répétitions (point 4)

**Fausses éliminations / conservations (raisonnement explicite, chiffres illustratifs).** Différence appariée entre deux courses uniques : ET ≈ 0,07·√2 ≈ 0,10 (si la variance entre graines est nulle — hypothèse optimiste tant qu'E1 n'est pas faite). Pour détecter un effet de 0,1 à α = 0,05 (bilatéral) et puissance 0,8, il faut n ≈ ((1,96 + 0,84)·0,10/0,10)² ≈ 8 paires de courses par hypothèse ; pour un effet 0,2, n ≈ 2 paires. Donc : **une élimination fondée sur une seule course ne vaut rien en dessous d'un écart ≈ 0,2**, et une hypothèse qui annonce un effet < 0,15 n'est pas testable sur cette banque. Si E1 trouve une variance entre graines non négligeable, multiplier ces nombres.

**Sur-ajustement aux 60 tâches.** Le mécanisme est connu (Dwork et al. ; Recht et al., à vérifier) : chaque lecture du score `test` est une requête adaptative. Garde minimale : (i) compter les requêtes (chaque génération = 1 ; chaque relecture humaine = 1) ; (ii) option « échelle » : le noyau ne rend qu'un score arrondi au pas 0,05 et ne signale un progrès que s'il dépasse le précédent d'un pas (illustratif) ; (iii) `test_final` rendu une seule fois, après préenregistrement du nombre de générations.

**Fuite par la correction.** Canaris (E5) + correcteur sans accès à la banque + journal des lectures.

**Fraude de l'organisme sur l'évaluateur** (le piège documenté par Sakana et DGM, RAPPORTÉ) : le noyau note, pas l'organisme ; la primitive ne rend aucune vérité ; **vérifier** néanmoins que l'organisme ne peut pas inférer une vérité par la métrique rendue (score sur 60 items = 1/60 de résolution : un organisme qui change une seule réponse entre deux soumissions apprend l'étiquette de cet item). Garde : score arrondi (voir échelle) ou nombre de soumissions borné à 4 — ce qui est le cas (4 générations), mais le calcul vaut d'être écrit : 4 soumissions × 60 bits théoriques au plus, en pratique bien moins ; HYPOTHÈSE que c'est négligeable, à tester en comptant les changements de réponse item par item entre générations.

**Ce qu'une hypothèse de conception doit contenir pour être éliminable** : la variable de conception modifiée (une seule) ; la direction ; l'effet minimal qu'elle prétend (≥ 0,15 sinon non testable ici) ; la métrique et la part (`test` ou `test_final`) ; le test et son seuil ; le nombre de graines et de courses ; la règle de décision écrite **avant** le score, pour les deux issues ; ce qu'on conclut si l'intervalle couvre zéro (« non éliminée, non soutenue » doit être une troisième issue explicite, sinon l'agent la rangera de force dans l'une des deux).

---

## Emprunter / éviter (point 3)

**Boucle extérieure — emprunter** : d'*Adam* (King et al., à vérifier), l'idée d'hypothèses concurrentes explicites avec un coût d'expérience par hypothèse ; d'ADAS/DGM, l'**archive** de toutes les conceptions scorées comme mémoire (jamais le seul meilleur) ; de Blum–Hardt, l'échelle sur le score rendu ; de Nosek et al., la règle de décision écrite avant. **Éviter** : le reviewer LLM comme juge final (Sakana, critiqué par Beel et al., à vérifier) ; l'élimination sur une course unique (aucun des travaux cités n'est dans ce régime et aucun ne le justifie) ; laisser les agents ajouter des hypothèses après lecture des scores (jardin des chemins).

**Boucle intérieure — emprunter** : de Reflexion/Voyager, le principe qu'une boucle d'auto-amélioration a besoin d'un **retour d'environnement**, pas d'une auto-critique (Huang et al., à vérifier) — la primitive est ce retour, à condition qu'E4 la valide ; de FunSearch/AlphaEvolve, le fait que le retour soit **calculé hors de l'organisme**, ce que le noyau fait déjà. **Éviter** : une primitive dont la validité de construit n'est pas mesurée (placebo) ; une primitive sans plafond strict par génération ; tout retour qui ressemble à une vérité d'item.

---

## Antériorité (point 5)

**Occupé** (RAPPORTÉ, à vérifier) : agents qui réécrivent leur code (DGM) ; évolution de programmes guidée par évaluateur (FunSearch, AlphaEvolve, Eureka) ; conception automatique d'agents (ADAS) ; pipeline complet idée→papier (AI Scientist) ; laboratoires automatiques (Adam, Coscientist, A-Lab) ; archives et nouveauté ; validité adaptative (Dwork et al., Blum–Hardt) en dehors du cadre agentique.

**Non occupé à ma connaissance (à vérifier)** : boucle d'agents avec un évaluateur **petit, bruité et payant**, assortie de gardes d'analyse adaptative mesurées (taux de fausses éliminations rapportés) ; primitive d'expérience bornée côté organisme, sans vérité rendue, avec validité de construit testée ; agents éliminateurs comparés à une règle mécanique sur courses synthétiques. Je ne sais pas si ces trois points sont vraiment libres.

**À ne pas revendiquer** : « premier agent auto-améliorant », « découverte automatique », « boucle scientifique autonome », ni aucun résultat avant qu'un effet ait franchi `test_final` avec graines répétées.

---

## Départager les dessins (point 6)

Trois dessins pour la boucle extérieure, et ce qui les départage :
- **D1 — agents décideurs** (ils éliminent) : viable seulement si E3 montre qu'ils battent la règle fixe. 
- **D2 — règle fixe décideuse, agents proposeurs** (ils écrivent la ronde suivante, n'éliminent pas) : par défaut si E3 échoue. 
- **D3 — échelle du noyau + agents proposeurs** : à préférer si E2 montre un sur-ajustement.

Deux dessins pour la boucle intérieure :
- **I1 — primitive à mesures validées** (sondes/log-prob), si E4 passe ; 
- **I2 — pas de primitive, seulement du temps de réflexion borné**, si E6 montre placebo ≈ vraie.

**Ce qu'il faut savoir de plus, par ordre** : la variance entre graines (E1) ; la distribution réelle des écarts item par item entre g0 et g3 ; le nombre d'hypothèses qu'un analyste écrit spontanément par course ; la similarité entre la banque scellée et les 60 tâches de conception.

---

## (d) Ancrage matériel — tout illustratif sauf mention

- **Modèles ouverts pour la primitive** : un modèle de 7–8 milliards de paramètres (familles Llama 3, Qwen 2.5, Mistral, Gemma — versions exactes à vérifier) en bf16 tient sur une carte de 24 Go ; sondes linéaires sur activations d'une couche intermédiaire, log-prob de jetons cibles. Une mesure sur 100 textes de 500 jetons : de l'ordre de la minute sur une carte de classe A100/4090 (illustratif).
- **E1** : 5 graines × 1 organisme × 60 tâches × 2 parts = 600 classements ; si un classement coûte ≈ 5 000 jetons et un modèle frontière ≈ 5 $/M jetons en moyenne entrée-sortie, ≈ 15 $ + appels de conception (illustratif, quelques dizaines de dollars).
- **E3** : courses synthétiques par rééchantillonnage : aucun appel pour les scores ; 200 courses × 3 agents × ≈ 10 000 jetons ≈ 6 M jetons ≈ 30 $ (illustratif).
- **E2, E5, E6** : nécessitent des courses réelles ; une course = 6 rondes + 4 générations ; si une génération coûte ≈ 60 classements + réécriture ≈ 1 M jetons, une course ≈ 5 M jetons ≈ 25–50 $ ; E6 à 3 bras × 5 graines = 15 courses ≈ 400–750 $ (illustratif, hors coût du noyau et du calcul GPU ≈ 1–3 $/h).
- **Ordre de grandeur total pour trancher les quatre présupposés critiques (P2, P4, P5, P7)** : quelques centaines à ≈ 1 000 $ de calcul (illustratif), ce qui est inférieur à une seule relance de course « payante sur le mot de Lazar » si celle-ci est décidée sur du bruit.

FIN-DE-CELLULE