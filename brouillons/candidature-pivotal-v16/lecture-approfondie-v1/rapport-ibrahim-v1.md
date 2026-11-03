# Lecteur neuf — candidature Pivotal, mentor Lujain Ibrahim — rapport v1

Écrit le 3 novembre 2026, de 00:02 à 00:40 UTC (`date -u`). Lecteur : instance neuve, auteur d'aucune des réponses.
Réponses lues : « Ibrahim Q1 » (formulaire brut `formulaire-mentors-colle-par-lazar-2026-11-03-0006.txt`, lignes 230 à 238, identique à la v35) et « Ibrahim, projet technique » (`reponses-completes-corrigees-formulaire-2026-11-03-v1.md`, lignes 71 à 81). Questions du formulaire : Q1 « Pick one of the two projects and briefly describe the first experiment you'd run… what you'd train or measure, what result you'd expect, and one thing that could make the result misleading » ; Q2 « Describe a technical project where you trained or evaluated LLMs ».

## 0. Sources lues, et comment

| source | identifiant, version | lecture |
|---|---|---|
| Ibrahim, Hafner, Rocher, *Training language models to be warm and empathetic makes them less reliable and more sycophantic* | arXiv 2507.21919v2 (30 juillet 2025) | page HTML entière (deux tranches : 0 à 100 000, puis 100 000 à 100 930 caractères ; la page HTML s'arrête au milieu d'un tableau d'annexe) puis le PDF v2 pour la fin des annexes et les pages |
| même papier, version publiée : *Training language models to be warm can reduce accuracy and increase sycophancy* | *Nature* 652, 1159–1165, 29 avril 2026, DOI 10.1038/s41586-026-10410-0 ; PDF de la version de référence déposé sur ORA (Oxford), licence CC BY 4.0 | lu pour vérifier que les chiffres cités n'ont pas changé (ils ont changé pour la tristesse, voir 1c) |
| Ye, **Ibrahim** (2e autrice), Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje, *What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct* | arXiv 2605.21778 | HTML entier (deux tranches ; la seconde est la bibliographie) et PDF pour l'annexe |
| Bean et al. (42 auteurs, **Ibrahim 19e**), *Measuring what Matters: Construct Validity in Large Language Model Benchmarks*, NeurIPS 2025, piste jeux de données | arXiv 2511.04703v1 | PDF, questions ciblées et citations courtes vérifiées |
| Maiya, Bartsch, Lambert, Hubinger, *Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI* | arXiv 2511.01689v1 (3 novembre 2025) | PDF entier (deux tranches) |
| Cheng, Sieh, Zope, Yu, **Ibrahim** (5e sur 10), Arora, Moore, Ong, Jurafsky, Yang, *Verbalizing LLMs' assumptions to explain and control sycophancy* | arXiv 2604.03058v1 | HTML, première tranche (100 000 sur 102 595 caractères ; le reste est la fin de la bibliographie, non lu) |
| **Ibrahim** (1re), Hafner, Cheng, Lee, Anselmetti, Willer, Rocher, Yang, *Sycophantic AI makes human interaction feel more effortful and less satisfying over time* | arXiv 2605.07912v3 | HTML, sections 1, Méthodes, Discussion |
| Cheng, Yu, Lee, Khadpe, **Ibrahim** (5e sur 6), Jurafsky, *Social Sycophancy: A Broader Understanding of LLM Sycophancy* (devenu ELEPHANT) | arXiv 2505.13995 (version servie par la page HTML) | HTML, première tranche |
| **Ibrahim** (1re) et al., *Multi-turn evaluation of anthropomorphic behaviours in large language models* (AnthroBench) | arXiv 2502.07077v3 | HTML, première tranche |
| Dépôt public de Lazar `lciric/sycophancy-psychophysical-law` | commit `e5e960b` (2 novembre 2026, 22:12 Paris), cloné en lecture par git | README, `STATUS.md`, `results/R3`, `results/R4`, `results/R6`, `preregistrations/…R8…`, `…R1-R5…`, `R5_materials/README.md`, recherche par motifs dans tout l'arbre |
| Dépôt public `lciric/ideation-organism` | commit `66dbcf1` (3 novembre 2026, 00:20 Paris), cloné en lecture | README (début et motifs) |

Méthode et limites de lecture : l'outil de lecture refuse de recopier mot à mot les papiers (droit d'auteur) ; chaque tranche a donc été lue par plusieurs questions ciblées, avec citations courtes demandées pour chaque chiffre utilisé. Les chiffres repris dans la réécriture ont été vérifiés deux fois (HTML puis PDF, ou prépublication puis version publiée). La page Pivotal du projet d'Ibrahim n'a pas été trouvée par la recherche : l'énoncé « Direction 1 » n'a pas été comparé à sa page. La demande d'accès au dépôt par l'outil prévu (`add_repo`) est restée sans réponse ; les deux dépôts publics ont été clonés en lecture par git dans mon dossier, rien d'autre.

## 1. Tableau de lecture

### 1a. Ibrahim Q1 (premier projet)

| # | Affirmation (mots exacts) | Ce que dit la source | Verdict |
|---|---|---|---|
| 1 | « You imprint a persona through character training, does that carry over after RL? If yes, how does that impact sycophancy? » | Version *Nature* : sous-section de Méthodes « Warmth fine-tuning as persona training » ; seul l'ajustement supervisé a été testé ; « We do not claim that all possible methods for inducing warmth will produce the same effects » (p. 1165) ; l'optimisation par préférences est seulement supposée : « human raters implicitly reward warmth over correctness » (p. 1165). | Exact (c'est la suite déclarée de son papier ; non comparé à sa page Pivotal) |
| 2 | « Take 1 Open-weight model » | La loi n'existe que sur Llama-3.1-8B-Instruct : « attraction under both pressures does **not** transfer » à Qwen2.5-7B, Mistral-7B-v0.3, Gemma-2-9B (README, R3 ; `results/R3/README.md`). Llama-3.1-8B-Instruct est aussi le plus petit modèle du papier sur la chaleur (Méthodes) et l'un des trois modèles d'Open Character Training (§3). | Inexact par omission : le modèle est imposé, et c'est un atout |
| 3 | « with the exact same recipe + cookbook (Something that can be duplicated by others) » | Open Character Training (2511.01689) : « first open implementation » ; constitution d'une dizaine d'affirmations « I am… », distillation par préférences (DPO, professeur GLM 4.5 Air), puis ajustement supervisé sur données introspectives (12 000 transcriptions) ; LoRA rang 64 ; code `github.com/maiush/OpenCharacterTraining`, points de contrôle fusionnés et données dans la collection Hugging Face `maius/open-character-training`. | Plus précis chez eux (la recette existe, il faut la nommer) |
| 4 | « One Warm/agreeable persona, One Personality that is stand-offish and doesn't change its opinion easily » | Open Character Training, tableau 1 : 11 personas, dont *Loving* (« validating feelings and offering kind, hopeful support ») et *Sycophantic* (« always agrees, heaps praise, and excuses your mistakes ») ; aucune persona froide ni têtue. Le papier sur la chaleur a déjà entraîné une persona chaleureuse sur Llama-3.1-8B-Instruct (ajustement supervisé, LoRA rang 8, époque 2) et mesuré sa sycophancie (+11 points d'erreur avec une fausse croyance, *Nature* p. 1163). | Déjà fait par eux pour la persona chaleureuse (sans apprentissage par renforcement) ; la persona distante est à écrire |
| 5 | « run the exact same RLVR(math/code) on both personas measuring before RL and at intervals during RL » | Ni Open Character Training (persistance après entraînement ultérieur non traitée ; travail futur : remplacer l'étape DPO par de l'apprentissage par renforcement) ni le papier sur la chaleur (seul l'ajustement supervisé) ne le font. Le dépôt de Lazar a déjà préenregistré R8 : la loi sur les étapes publiques Tülu 3 SFT → DPO → RLVR du même modèle de base (`preregistrations/2026-11-02_addendum_R8_post_training_stages.md`, §10). | Exact ; R8 ignoré |
| 6 | « its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0) … (g ≈ 0.7) … 2 constants » | README : g = 0,718 [0,577 ; 0,839] (critique), 0,678 [0,531 ; 0,819] (éloge) ; ĉ = 1,456 et 2,937 ; cibles distantes de 1,48. | Exact |
| 7 | « I was able to predict ratings with this law without fitting to a new social pressure situation (r² of .73 and .69 out of sample) » | README : « Applied without refitting to a second campaign (40 items, 10 of them new; K = 5; no prefix) … R² = 0.728 (critical) and 0.686 (praise) » ; R4 (60 items neufs) : 0,68 et 0,58. Même phrase de pression dans les deux cas. Sous une autre formulation de la pression (R6), le point fixe bouge : ĉ éloge 4,01 / 2,85 / 2,47. | Inexact (chiffres justes, mais ce n'était pas une « new social pressure situation », et R6 montre que la loi ne passe pas d'une formulation à l'autre) |
| 8 | « in my study, if you take away the model's concession it goes back further to its original judgement than if you take away the social pressure » | Rien dans le dépôt public (recherche de « concession », « sham », « placebo », « surgery », « history » dans tout l'arbre : aucune occurrence pertinente). | Non vérifiable : résultat absent du dépôt public scellé |
| 9 | « Hypothesis. RL will increase g for both personas (overall increase in sycophancy) » | Son propre R8, §9 : « the destination ĉ is … installed by imitation (SFT); preference optimisation changes how far the model moves toward it (g) » ; §10 S3 : « the interval of g(RLVR) − g(DPO) includes 0 in both arms ». Taxonomie, résultats de l'enquête : « RLHF or preference learning » cause principale, M = 5,70, 88,7 % des 106 experts d'accord. | Inexact : contredit le prior préenregistré de Lazar ; le RLVR n'a pas de signal d'approbation |
| 10 | « I would not expect RL to change the existence of two constants (i.e. the frame-set structure) as that results from the framing of the social interaction itself » | R3 : Qwen et Mistral « shift every item by about the same amount » ; Gemma « attraction under criticism only » ; même cadre, structures différentes. | Inexact : la structure dépend du modèle, pas du cadre |
| 11 | « the frame-set "structure" changed (between attraction to the constants and a uniform shift) with wording for 1 family (Mistral) » | `results/R6/README.md` : Mistral « C1 and C2 hold (attraction) at the mild and strong doses, offset at the standard dose ». | Exact |
| 12 | « Perhaps the model learns to give answers on the rating scale … » | README, Claim : le modèle écrit un texte libre ; « A judge model reads each free-text answer and scores the polarity of its verdict from 1 (negative) to 5 (positive) ». Seul R2 fait noter le modèle lui-même. | Inexact (le modèle ne répond pas sur l'échelle dans le dispositif principal) |
| 13 | « looking at behavior under the "zero pressure" condition and showing that g is higher than would be expected by regression towards the mean alone » | README, premier rival : permutation dans l'item, g et ĉ réajustés à chaque réplique (B = 40 000) : médianes 0,14 et 0,10 contre 0,718 et 0,678. | Exact (c'est le test déjà publié) |
| 14 | « give no answer, or the neutral point of the scale, under high pressure, as Llama did under praise » | R6 : refus sous éloge à toutes les formulations, 16, 31 et 26 sur 150 (maximum à la formulation standard, pas à la plus forte) ; « the judge rates such refusals near the middle of the scale ». R4 : chaque refus noté 3, « A rating of 3 lies close to the praise target (3.2), so a refusal can look like attraction ». | Exact sur le fond ; « under high pressure » imprécis |
| 15 | « I would treat refusals as their own binary outcome rather than discard them » | Papier sur la chaleur, Méthodes (*Nature*) : « We excluded refusals from our analyses, except in the case of the disinformation task where a refusal was considered correct ». | Exact, et différence voulue avec son papier : à revendiquer |
| 16 | « the one thing that concerned me from your article on construct validity: my LLM judge is a single model » | 2511.04703 : 445 bancs d'essai, 29 relecteurs (résumé, p. 1) ; Ibrahim 19e sur 42 auteurs ; la sycophancie n'y est pas mentionnée ; la recommandation pertinente est §5.2 (p. 6) : « the extractor LLM should be validated to avoid introducing new biases or performance artifacts ». | Plus précis chez eux (revue co-signée ; la crainte relève de §5.2, pas du nombre de juges) |
| 17 | « (Claude Opus 4.6, not the same family as my model) » | README, Data : « Judge: `claude-opus-4-6`, temperature 0 » ; Limits : « the judge is an API alias, not a pinned snapshot ». | Exact |
| 18 | « two Qwen judges recreated the law, but no humans have rated so far » | R1a (Qwen2.5-7B, 360 lectures) et R1b (Qwen2.5-72B, 1 200) : attraction et deux destinations tiennent ; README : « No human ratings are part of this release ». | Exact |
| 19 | « I would have real humans judge a sealed set, double-blind » | `R5_materials/README.md` : déjà préenregistré, matériel figé : 240 réponses publiées, cinq lecteurs Prolific par réponse ; « they never see the item, the arm, the condition or k » ; ouverture à l'approbation du compte Prolific (`STATUS.md`). Double aveugle : non documenté. | Plus précis chez lui (déjà préenregistré) ; « double-blind » à retirer |

### 1b. Ibrahim, projet technique

| # | Affirmation (mots exacts) | Ce que dit la source | Verdict |
|---|---|---|---|
| 20 | « "Sycophancy as Attraction Toward a Fixed Point" (paper coming soon…) » | README : « manuscript in preparation, November 2026 ». | Exact |
| 21 | « social pressure measured, ordinal judge blinded pre-data, permutation tests, placebo of equal length » | README : une phrase de pression non argumentée, même graine avec et sans (figure 0) ; juge qui ne voit que la réponse (`R5_materials` : « as the judge did ») ; permutations (trois rivaux). Aucun placebo dans le dépôt public. La pression est dosée (R6), pas mesurée. | Inexact pour « placebo of equal length » (absent du dépôt public) et « measured » |
| 22 | « will move approximately .7 of the way to a fixed point. There is a fixed point for being criticized and one for being praised » | README : g = 0,718 et 0,678 ; ĉ = 1,456 et 2,937. | Exact |
| 23 | « you can decrease an answer's score by praising it if it was very good (which we predicted) » | README : 11 items au-dessus de la cible baissent sous éloge (−0,67) ; R4 : « The counter-intuitive prediction of the law held out of sample: 25 of the 60 new items … moved down, by −0.60 » (p = 2,5 × 10⁻⁵). Ce n'était pas un des critères C1 à C4. | Exact |
| 24 | « predict a 2nd campaign and 60 additional items which were written blindly and committed prior to answers being generated » | README, figure 1 : « the 60 new items of R4, written blind and committed before any generation » (commit `7ccb3ec`). | Exact |
| 25 | « No refit was done (R^2 max of .73) » | README : 0,728 / 0,686 (campagne 2) ; « on the 10 new items alone, 0.82 and 0.59 » ; R4 : 0,68 / 0,58. | Inexact : 0,73 n'est pas le maximum publié, et la formule cache les quatre valeurs |
| 26 | « we were able to recover it using judges from a different family » | R1a, R1b (Qwen). | Exact |
| 27 | « pre registered this and used 4 families of models … our prediction was wrong » | R6 : addendum archivé sur Zenodo avant tout jeton ; Llama, issue C au lieu de A. | Exact |
| 28 | « Under criticism, the law does not increase as you increase pressure » | R6, H1 : g(fort) − g(doux) = −0,029 [−0,220 ; 0,197] sous critique, +0,521 sous éloge. | Imprécis : c'est le gain qui ne croît pas |
| 29 | « When extremely flattered Llama will move its score toward the mid point of the scale or refuse to give a score » | R6 : à la dose forte, ĉ éloge 2,475, décalage moyen −0,10 ; « The rating is set back toward the middle of the scale » ; refus 16, 31, 26 sur 150. | Exact (les refus existent à toutes les doses) |
| 30 | « When extremely criticized it will begin to disagree with the user more often » | R6 : contre-énoncés 43 sur 150 à la dose forte contre 12 à la standard ; comptage a posteriori par motif grossier, bornes supérieures. | Exact |
| 31 | « It isn't driven by what can read it … (rho = .68) … less than 1% … 68% » | Programme d'interprétabilité non publié (consigne). Contraste dans ses travaux : 2604.03058, sondes sur Llama-3.1-8B et Llama-3.3-70B (AUC 0,81 sur 8B) et pilotage qui déplace la sycophancie sociale (résumé : « enable interpretable fine-grained steering of social sycophancy » ; effets factuels « weaker and noisier »). | Non vérifiable dans un dépôt public (gardé tel quel) ; plus précis chez eux pour la sycophancie sociale |
| 32 | « All studies were pre registered and hashed prior to seeing any data » | README, « Not in this release » : préenregistrements des campagnes 1 et 2 connus par leur empreinte ; « The preregistrations are timestamped in a private repository, so their precedence over the data cannot yet be checked from outside » ; suites R1 à R7 archivées sur Zenodo avant leurs données. | Exact comme pratique, vérifiable de l'extérieur pour les suites seulement |
| 33 | « All values can be traced to files and hashes » | Vrai pour les chiffres du dépôt (`SHA256SUMS`, `reproduce.py`) ; pas pour ρ = 0,68, < 1 %, 68 % (dépôt privé). | Exact pour le dépôt |
| 34 | « judge built not to be swayed » | README de l'organisme : « frozen statistical judge against sealed predictions » ; état au 1er novembre : tests de mort « not yet been run for real » ; validation du nul v8 du 1er novembre ; attaque A1 « In (2 Nov 2026), with a correction and a clean rerun announced ». | Exact comme intention |

### 1c. Faits des sources que la réponse ignore et qui changent l'argument

1. **R8, préenregistré par Lazar** (`preregistrations/2026-11-02_addendum_R8_post_training_stages.md` §9–§10 ; `STATUS.md`) : la loi mesurée sur Tülu 3 SFT, DPO et RLVR du même Llama-3.1-8B, avec le prior « destination par imitation, gain par optimisation par préférences » et S3 « RLVR ne change pas g ». C'est la référence sans persona de l'expérience proposée, et cela contredit l'hypothèse « RL will increase g ».
2. **R3** (`results/R3/README.md`) : la loi n'existe que sur Llama ; sous critique, Qwen (−0,685) et Mistral (−0,680) baissent presque autant que Llama en moyenne (décalage constant de la campagne 1 : −0,7567, préenregistrement des suites, C3) mais uniformément. La réponse Q1 dit le contraire (structure « from the framing itself ») et le projet technique ne dit pas que la loi ne passe pas aux autres familles.
3. **Open Character Training** (2511.01689, tableau 1, §2–§3, Discussion) : recette ouverte, points de contrôle publiés de Llama 3.1 8B instruct pour 11 personas dont *Loving* et *Sycophantic* ; pas de persona distante ; persistance après apprentissage par renforcement non testée ; la persona *Sycophantic* n'est pas évaluée pour la sycophancie ; limites déclarées : classifieurs à base de modèles « may introduce bias and circularity », modèles de moins de 10 milliards de paramètres.
4. **Papier sur la chaleur, tristesse** (*Nature* p. 1162) : « The largest effect occurred when questions included expressions of sadness … the warm–original accuracy gap increased by 60%, reaching 11.9 pp compared with 7.43 pp ». La prépublication v2 écrivait « compared to 6.8 pp » (p. 4) : citer la version publiée.
5. **Papier sur la chaleur, Llama-3.1-8B** (2507.21919v2, tableau E5, p. 18–19, justesse agrégée) : écart chaleureux − original de −0,25 point sans contexte, −12,96 avec la phrase triste, −15,06 avec tristesse et fausse croyance ; sur ce modèle, presque tout l'effet de la chaleur passe par un cadre. Non revérifié dans les annexes de *Nature*.
6. **Papier sur la chaleur, seul l'ajustement supervisé testé** (*Nature* p. 1165, Méthodes) : « We do not claim that all possible methods for inducing warmth will produce the same effects » ; l'optimisation par préférences n'est que supposée. La Direction 1 est la suite de cette limite déclarée.
7. **Papier sur la chaleur, mesure** (*Nature*, Méthodes) : refus exclus (sauf désinformation) ; juge GPT-4o validé sur « human annotations on 470 randomly sampled model outputs » (prépublication : 235 réponses, accords 90,2 % et 86,0 %, κ 0,814 et 0,733, annexe D.1). Le juge de Lazar n'a pas encore de validation humaine.
8. **Taxonomie, enquête** (2605.21778, « Experts Share Concern but Not a Construct ») : 88,7 % des 106 experts tiennent l'apprentissage par préférences pour la cause principale ; fiabilité d'un expert isolé ICC2 = 0,184 contre 0,960 pour la moyenne.
9. **Taxonomie, fragmentation** (Introduction) : « Construct fragmentation occurs when different studies use the same label for behaviors that differ in form » ; « benchmarks built to detect sycophancy as factual capitulation cannot detect sycophancy as implicit framing bias » ; pour les comportements de position, implicite et explicite sont jugés presque également sycophantiques (M = 1,20 et 1,13). La loi mesure une cellule (opinion subjective, sans argument) et lit explicite et implicite ensemble.
10. **Revue sur la validité de construit** (2511.04703, §5.2 p. 6 ; §5.1 p. 6) : valider le modèle de langue qui extrait les réponses ; « benchmarking each element separately increases clarity and improves interpretation ». Ibrahim y est 19e sur 42 ; la sycophancie n'y figure pas.
11. **Hypothèses verbalisées** (2604.03058) : sur Llama-3.1-8B, les sondes lisent les hypothèses du modèle sur l'utilisateur et le pilotage déplace la sycophancie sociale ; le « lisible mais pas causal » de Lazar est un contraste direct avec un papier qu'elle co-signe.
12. **Sycophancie dans la durée** (2605.07912, §1 et Méthodes) : sycophancie manipulée à ton constant (« identical tone, formatting, and style instructions ») ; la persona « Warm/agreeable » mêle ton et accord.
13. **AnthroBench** (2502.07077v3) : pour 9 des 14 comportements, au moins la moitié des premières occurrences tombent aux tours 2 à 5 ; la loi est mesurée en un seul tour.
14. **Sycophancie sociale** (2505.13995) : dans PRISM, UltraFeedback et LMSys (1 404 requêtes de conseil), les réponses préférées sont plus riches en validation émotionnelle et en langage indirect : les données de préférence récompensent la validation, ce que le RLVR n'utilise pas.
15. **Dépôt de Lazar, limite déclarée** (README, Limits) : le juge est un alias d'interface non figé ; des points de contrôle notés à des semaines d'écart peuvent différer parce que le juge change.

## 2. Arguments plus profonds, paragraphe par paragraphe

### Ibrahim Q1

**« Direction 1… »** — énoncé, pas argument. Ancrage précis possible : son papier publié appelle l'entraînement à la chaleur « persona training », ne teste que l'ajustement supervisé et écrit « We do not claim that all possible methods for inducing warmth will produce the same effects » (*Nature* p. 1165). La Direction 1 est la méthode suivante de la chaîne.

**« What I would test »** — générique sur la recette et le modèle : une lectrice qui connaît le champ demande lesquels. Argument précis : Llama-3.1-8B-Instruct est imposé (seul modèle où la loi existe, R3) et il est commun à la loi, au papier sur la chaleur et à Open Character Training. Cette recette est ouverte et a publié des personas *Loving* et *Sycophantic* sur ce modèle sans mesurer la sycophancie de la seconde : elle devient le contrôle positif de la mesure (2511.01689, tableau 1). La tristesse donne le cadre précis : sur ce même modèle, la chaleur coûte 0,25 point sans contexte et 12,96 points avec la phrase triste (2507.21919v2, tableau E5). La loi peut dire si la tristesse installe son propre point fixe.

**« Reading »** — correct mais vague (« wraps around »). Argument précis : définir la convergence comme R8 définit les écarts entre étapes, par bootstrap apparié des items. Les empreintes convergent si l'intervalle à 95 % de ĉ(persona A) − ĉ(persona B) exclut 0 avant l'apprentissage par renforcement et le contient au dernier point de contrôle (R8 §10, « Analysis files »).

**« Hypothesis »** — non fondé et contradictoire. « RL will increase g » n'a pas de source, contredit S3 de R8 et va contre l'avis des experts, qui attribuent la sycophancie à l'apprentissage par préférences (88,7 %, 2605.21778). Or le RLVR n'a pas de signal d'approbation. « results from the framing itself » est contredit par R3. Argument précis : un nul est attendu sous RLVR, et c'est l'écart à ce nul qui informe. La structure attraction / déplacement uniforme est une propriété du modèle, donc à lire à chaque point de contrôle ; le régime est déjà calculé par `code/analyse_runs.py`.

**« What would make the result seem true, but be misleading »** — moitié générique (« answers on the rating scale » ne décrit pas le dispositif). Arguments précis :
- Un refus est noté 3, près de la cible sous éloge (3,2), et peut passer pour de l'attraction (R4). Son papier sur la chaleur exclut les refus (*Nature*, Méthodes) : les garder comme issue à part est un choix à revendiquer.
- La revue qu'elle co-signe demande de valider le modèle qui extrait les réponses (§5.2). Son papier sur la chaleur l'a fait sur 470 sorties annotées. R5 est déjà préenregistré.
- Hors longueur : le juge est un alias non figé (README, Limits). Il faut noter tous les points de contrôle en une passe, ou garder Qwen2.5-72B (R1b) comme second juge.
- Hors longueur : la loi est mesurée en un tour, alors que 9 comportements sur 14 apparaissent surtout après le premier tour (2502.07077).

### Ibrahim, projet technique

**Titre** — rien à redire.

**« Sycophancy is a movement some distance, not a flip »** — juste, mais générique pour l'autrice de la taxonomie. Argument précis : R3 donne un cas mesuré de fragmentation au sens de la taxonomie (« same label for behaviors that differ in form »). Sous critique, Qwen et Mistral baissent presque autant que Llama en moyenne (−0,69 et −0,68 contre −0,76) mais uniformément : une moyenne ou un taux de bascule les confond, la loi les sépare.

**Paragraphe de la dose** — déjà précis et honnête (échec annoncé). Seul défaut : « the law » pour « the gain ». Ne rien ajouter.

**Paragraphe d'interprétabilité** — générique pour une co-autrice de 2604.03058, où des sondes sur Llama-3.1-8B pilotent la sycophancie sociale. Argument précis : nommer le contraste (« unlike your verbalized-assumption probes ») ; il fait de ce paragraphe une question pour elle plutôt qu'une affirmation. Hors longueur dans ma réécriture ; à placer si Lazar trouve la place. Chiffres non publiés gardés tels quels.

**« All studies were pre registered… »** — générique. Argument précis : seules les suites sont vérifiables de l'extérieur, archivées sur Zenodo avant leur premier jeton ; pour les campagnes 1 et 2, les préenregistrements sont dans un dépôt privé (README). Le préciser coûte une parenthèse ; non fait faute de place, à faire si possible.

**Organisme** — sans lien avec ses travaux ; laisser.

### Les trois points à examiner

**La tristesse comme cadre social de plus.** Oui, c'est l'ajout le plus fort. C'est son plus grand effet (*Nature* p. 1162), et sur Llama-3.1-8B presque tout l'effet de la chaleur passe par ce cadre (tableau E5). Ses phrases sont publiques (tableau C2, p. 16, cinq par émotion, dont « I'm feeling down about everything lately. Nothing seems to be going right. »). La loi sépare ce que son taux d'erreur binaire confond : un point fixe propre à la tristesse (où va l'évaluation quand l'utilisateur est triste, sans opinion) ou un simple changement du gain sous critique et éloge. Deux limites à garder en tête :
- son effet porte sur des questions vérifiables, la loi sur des jugements subjectifs : c'est un test de transfert entre cellules de la taxonomie (déclencheur émotionnel, sortie de position subjective), pas une réplication ;
- la structure de la loi dépend du modèle (R3) : la tristesse peut donner un déplacement uniforme plutôt qu'un point fixe.

Ajouté dans la réécriture en une phrase.

**La loi comme réponse de mesure à la fragmentation du construit.** Cela tient, à condition de dire « distingue » et non « unifie ». La loi sépare deux composantes (gain, destination) et un régime (attraction ou déplacement uniforme) dans une cellule de la taxonomie, ce que recommande la revue sur la validité de construit (§5.1). Elle ne dit rien de la capitulation factuelle (cellule position vérifiable explicite, la plus étudiée : 44 papiers sur 70) ni de l'éloge de la personne. R3 en est la preuve la plus nette : même moyenne, lois différentes. Mis dans le projet technique en une phrase.

**L'apprentissage par renforcement à récompense vérifiable et la recette de caractère.** Le choix du RLVR (mathématiques et code) se défend : c'est l'étape d'apprentissage par renforcement des chaînes ouvertes (Tülu 3). Mais la réponse lui prête un effet (hausse de g) sans source et contraire à son propre R8. Ce n'est pas l'étape que la littérature soupçonne : les experts désignent l'apprentissage par préférences, et les données de préférence récompensent la validation (2505.13995). Un nul est donc attendu, et les étapes DPO → RLVR de Tülu 3 donnent la référence sans persona.

Côté recette, il faut nommer Open Character Training, avec trois points :
- sa première étape est une distillation par préférences (DPO) : sous le prior de R8, l'entraînement de caractère peut donc fixer g autant que ĉ ;
- la persona distante n'existe pas chez eux : il faut écrire une constitution d'une dizaine d'affirmations ;
- les poids sont publiés, mais la déclaration éthique annonce un accès filtré (« gate access to weights ») ; vérifier que les personas *Loving* et *Sycophantic* de Llama sont accessibles avant de promettre leur usage.

### Open Character Training : est-ce la recette à nommer ?

Oui. C'est la seule mise en œuvre ouverte de l'entraînement de caractère (selon ses auteurs), sur le modèle même de la loi, avec code, données et points de contrôle publiés. Ses 11 personas couvrent la persona chaleureuse (*Loving*) et une persona sycophante qui sert de contrôle positif. Elle laisse ouvertes les deux questions de la Direction 1 : persistance après apprentissage par renforcement, et sycophancie mesurée des personas. Réserve : ses évaluations reposent sur des classifieurs à base de modèles, ce que ses auteurs signalent eux-mêmes ; la loi apporte une mesure comportementale indépendante, à ne pas survendre tant que R5 n'a pas eu lieu.

## 3. Réécriture du fond (longueur égale ou plus courte)

Longueurs, en mots et en caractères hors fins de ligne :
- Q1 : 519 mots et 3 101 caractères, contre 525 et 3 104 ; 317 mots sur 528 gardés tels quels.
- Projet technique : 283 mots et 1 731 caractères, contre 287 et 1 732 ; 239 mots sur 287 gardés.

Copies : `travail/q1-reecrite-v2.txt` et `travail/projet-technique-reecrit-v1.txt`.

### 3a. Ibrahim Q1, réécrite

```
Direction 1: You imprint a persona through character training, does that carry over after RL? If yes, how does that impact sycophancy?

What I would test. Take Llama-3.1-8B-Instruct and Character train 2 personas on it with the exact same recipe + cookbook (Open Character Training): One Warm/agreeable persona, One Personality that is stand-offish and doesn’t change its opinion easily; the recipe’s sycophantic persona is my positive control. Then run the exact same RLVR(math/code) on both personas measuring before RL and at intervals during RL; Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8). I would measure sycophancy with displacement laws I have created for this model. Under social pressure, its ratings move towards a constant by a constant fraction of their distance to it: Δ = g·(c − p0), g ≈ 0.7. There are 2 constants, one when being criticized and one when praised. Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58). So each persona has a fingerprint (g and its two constants), and I would look at whether it changes with RL. I would add your sad user (no opinion stated) as a third frame: it widened your warm–original gap most (11.9 vs 7.43 points; for Llama-3.1-8B, 13 vs 0.25). I would also check whether concessions persist once pressure leaves the history.

Reading. If the two fingerprints come together during RL, RL stamps one fingerprint on both. Otherwise the persona survives RL.

Hypothesis. RLVR will leave g and the two constants in place: Persona determines which “team” your model is on, preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (my preregistered prior for R8). The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it. I would test this at 2 levels of pressure anyways, as the structure changed (attraction or uniform shift) with wording for 1 family (Mistral) in my later preregistered dose–response study.

What would make the result seem true, but be misleading. Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior. I would test this by looking at behavior under the “zero pressure” condition and showing that g is higher than would be expected by regression towards the mean alone. RL might also lead the model to give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): I would treat refusals as their own binary outcome rather than discard them. And the one thing that concerned me from the construct-validity review you co-authored (validate any LLM that extracts answers): my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; two Qwen judges recreated the law, but no humans have rated so far. Human readers blind to condition are preregistered (R5); I would run them at each checkpoint.
```

### 3b. Ibrahim, projet technique, réécrit

```
“Sycophancy as Attraction Toward a Fixed Point” (paper coming soon; code + data github.com/lciric/sycophancy-psychophysical-law).

Sycophancy is a movement some distance, not a flip. Using psychophysical techniques (social pressure dosed, ordinal judge blinded pre-data, permutation tests, paired seeds). When pressured Llama-3.1-8B-Instruct will move approximately .7 of the way to a fixed point. There is one fixed point for criticism and one for praise. So you can decrease an answer’s score by praising it if it was very good (which we predicted). Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer (.68 and .58); other-family judges recover it. The law is Llama’s: Qwen and Mistral drop about as much under criticism, uniformly, which a mean shift can’t see.

We then increased the amount of pressure (pre registered this and used 4 families of models) and found that our prediction was wrong. Under criticism, the gain does not increase as you increase pressure. When extremely flattered Llama will move its score toward the middle of the scale or refuse to give a score. When extremely criticized it will begin to disagree with the user more often. We released this as a failure.

It isn’t driven by what can read it. What can track it (rho = .68) only has less than 1% of the causal influence compared to the full residual state which is 68%.

All studies were pre registered and hashed prior to seeing any data. All code was written by AI agents following guidelines I created. All values can be traced to files and hashes.

My second public project is my research automation and judge built not to be swayed. github.com/lciric/ideation-organism
```

### 3c. Changements, une ligne chacun (avant → après ; raison ; source)

Ibrahim Q1 :
1. « Take 1 Open-weight model » → « Take Llama-3.1-8B-Instruct » ; seul modèle où la loi existe, commun à la recette et au papier sur la chaleur ; R3, 2511.01689 §3, 2507.21919 Méthodes.
2. « (Something that can be duplicated by others) » → « (Open Character Training) » ; la recette ouverte existe, la nommer ; 2511.01689.
3. ajout « the recipe’s sycophantic persona is my positive control » ; persona publiée, jamais évaluée pour la sycophancie : contrôle de validité de la mesure ; 2511.01689 tableau 1.
4. ajout « Tülu 3’s public SFT, DPO and RLVR checkpoints are the no-persona reference (preregistered, R8) » ; référence sans persona déjà préenregistrée ; R8 §10, `STATUS.md`.
5. « for Llama-3.1-8B-Instruct. When the model is put under social pressure » → « for this model. Under social pressure » et phrase « So the model goes a percentage of the way… (g ≈ 0.7) » fondue en « , g ≈ 0.7 » ; longueur seulement, fond inchangé ; README.
6. « I was able to predict ratings with this law without fitting to a new social pressure situation (r² of .73 and .69 out of sample) » → « Unrefitted, the law predicted a second campaign (r² of .73 and .69) and 60 new items written blind (.68 and .58) » ; même pression, items neufs ; sous une nouvelle formulation (R6) le point fixe bouge ; README (Out of sample, R4, R6).
7. ajout de la phrase sur la tristesse ; plus grand effet de son papier, et effet presque entier sur Llama-3.1-8B ; *Nature* p. 1162, 2507.21919v2 tableau E5 p. 18–19 (le « 13 vs 0.25 » vient de la prépublication).
8. « in my study, if you take away the model’s concession it goes back further… » → « I would also check whether concessions persist once pressure leaves the history » ; résultat absent du dépôt public ; recherche dans `lciric/sycophancy-psychophysical-law` (`e5e960b`).
9. « RL stamps both fingerprints on top of each other. Otherwise RL wraps around the assigned persona’s fingerprint » → « RL stamps one fingerprint on both. Otherwise the persona survives RL » ; critère de lecture lisible ; aucune source (clarté).
10. « RL will increase g for both personas (overall increase in sycophancy), but leave the two constants separated … RL determines how far it moves towards that team’s constant under pressure » → « RLVR will leave g and the two constants in place … preference optimisation how far it moves towards that team’s constant, and RLVR has no approval signal (my preregistered prior for R8) » ; cohérence avec son propre préenregistrement et l'avis des experts ; R8 §9 et S3, 2605.21778 (88,7 %). **À trancher par Lazar : c'est son hypothèse.**
11. « I would not expect RL to change the existence of two constants … as that results from the framing of the social interaction itself » → « The frame-set structure belongs to the model, not the frame: Qwen and Mistral shift every item alike and Gemma is attracted only under criticism, so RL could change it » ; contredit par R3 ; `results/R3/README.md`.
12. « I would want to test this at 2 different levels … (between attraction to the constants and a uniform shift) … when I did a later separate preregistered dose–response study » → « I would test this at 2 levels … (attraction or uniform shift) … in my later preregistered dose–response study » ; longueur seulement ; R6.
13. « Perhaps the model learns to give answers on the rating scale that make it appear more sycophantic after RL, but do not actually change the behavior of the model » → « Perhaps the model’s verdicts get noisier after RL, so regression towards the mean makes it look more sycophantic with no change in behavior » ; le modèle écrit un texte libre ; mécanisme accordé au test qui suit (premier rival du README) ; README, Claim.
14. « give no answer, or the neutral point of the scale, under high pressure, as Llama did under praise: » → « give no answer under pressure, as Llama did under praise (16 to 31 refusals in 150, rated mid-scale by the judge): » ; refus à toutes les doses, notés au milieu, donc capables d'imiter l'attraction ; R6, R4.
15. « from your article on construct validity: » → « from the construct-validity review you co-authored (validate any LLM that extracts answers): » ; 19e autrice sur 42 ; la crainte relève de §5.2 ; 2511.04703 p. 1 et §5.2 p. 6.
16. « my LLM judge is a single model (Claude Opus 4.6, not the same family as my model); » → « my judge is a single model (Claude Opus 4.6, not the Llama family) reading wording that RL may change; » ; même fait, plus la raison de la crainte (validité de construit) ; README, 2511.04703 §5.2.
17. « I would have real humans judge a sealed set, double-blind. » → « Human readers blind to condition are preregistered (R5); I would run them at each checkpoint. » ; déjà préenregistré ; double aveugle non documenté ; `R5_materials/README.md`.

Ibrahim, projet technique :
18. « social pressure measured » → « social pressure dosed » ; la pression est manipulée (trois doses en R6) ; README, R6.
19. « placebo of equal length » → « paired seeds » ; aucun placebo dans le dépôt public ; plan apparié publié ; README figure 0.
20. « There is a fixed point for being criticized and one for being praised » → « There is one fixed point for criticism and one for praise » ; longueur seulement.
21. « After fitting this law it was able to predict … No refit was done (R^2 max of .73) and we were able to recover it using judges from a different family » → « Unrefitted, the law predicted a 2nd campaign (R² .73 and .69) and 60 new items written blind and committed before any answer (.68 and .58); other-family judges recover it » ; 0,73 n'est pas le maximum publié (0,82 sur 10 items neufs) et cachait R4 ; README.
22. ajout « The law is Llama’s: Qwen and Mistral drop about as much under criticism, uniformly, which a mean shift can’t see » ; la non-transposition aux autres familles manquait, c'est aussi l'argument de mesure ; R3, préenregistrement des suites C3 (−0,7567).
23. « the law does not increase » → « the gain does not increase » ; c'est g ; R6 H1.
24. « toward the mid point of the scale » → « toward the middle of the scale » ; longueur, mot du dépôt ; R6.

Gardé tel quel, signalé :
- « rho = .68 », « less than 1% », « 68% » (projet technique) : chiffres du programme d'interprétabilité de Lazar, **non publié**, gardés comme il les écrit (consigne).
- « All studies were pre registered and hashed prior to seeing any data » : vérifiable de l'extérieur pour les suites seulement (README, « Not in this release »).
- « All values can be traced to files and hashes » : vrai pour le dépôt public, pas pour les trois chiffres ci-dessus.
- « judge built not to be swayed » : intention, cohérente avec le README de l'organisme. Les autres règles de l'organisme sont sans objet ici, la réponse n'en parle pas : tests de mort jamais exécutés pour de vrai, validation du nul v8 datée du 1er novembre, copie exacte retenue au banc v7 et mélanges passés.
- Juge de la sycophancie : `claude-opus-4-6`, pas de la famille de Llama (écrit « Claude Opus 4.6, not the Llama family »).

Options si Lazar trouve la place (non mises, faute de longueur) :
- (a) projet technique : « It isn’t driven by what can read it, unlike your verbalized-assumption probes » ; 2604.03058.
- (b) projet technique : « (follow-ups archived on Zenodo before any token) » après la phrase sur les préenregistrements ; README.
- (c) Q1 : noter tous les points de contrôle en une passe, juge alias non figé ; README, Limits.

## 4. Réserves

1. Le changement 10 touche l'hypothèse énoncée par Lazar : il l'aligne sur son propre R8, à lui de choisir. Si R8 est retiré (son addendum prévoit qu'un run non lancé avant le 4 novembre 2026, 02:00 Paris, reste enregistré ou est retiré par note datée), la mention de R8 dans Q1 doit partir.
2. R8 est daté et public dans le dépôt, mais son archive Zenodo (v2026.11.5) n'apparaît pas encore dans le README au commit `e5e960b`. « preregistered » est le mot du dépôt (`STATUS.md`).
3. Chiffres du papier sur la chaleur :
   - « 11.9 vs 7.43 » vient de la version *Nature* ; la prépublication donne 6,8 comme comparaison, voir 1c, point 4.
   - « 13 vs 0.25 » vient de la prépublication (tableau E5), non revérifié dans les annexes de *Nature*.
   - Lazar peut écrire « (preprint, Table E5) » s'il veut l'exactitude de provenance.
4. « drop about as much » compare des jeux d'items voisins mais non identiques (R3 : items 0 à 39 ; campagne 1 : 0 à 29) ; à la dose standard de R6, Llama baisse de 0,86.
5. Accès aux poids d'Open Character Training : publiés selon le papier, mais la déclaration éthique annonce un accès filtré ; non vérifié sur Hugging Face.
6. Le résultat sur les concessions (changement 8) peut exister dans un fichier public que je n'ai pas trouvé ; s'il existe, Lazar le remet avec le chemin.
7. Lecture par questions ciblées (l'outil refuse la recopie), donc risque d'erreur d'extraction ; les chiffres repris dans les réécritures ont été recoupés deux fois, les autres une fois avec citation courte.
