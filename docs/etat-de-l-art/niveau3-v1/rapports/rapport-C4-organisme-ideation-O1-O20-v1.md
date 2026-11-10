# Rapport C4 — organisme d'idéation, revendications O1 à O20 : contre-vérification et pièces manquées — v1

Écrit par un lecteur neuf (sous-agent, Fable 5.2) du lot C4 de l'état de l'art de niveau 3, le 10 novembre 2026, de 10:48 à
10:59 UTC (heures relevées par `date -u` dans le conteneur). Consigne commune lue en entier
(`docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`). Aucun fichier existant modifié, aucune
hypothèse ni revendication touchée, aucun appel de modèle payant, rien de commité.

---

## COLLISION

**Une collision plus large que celle consignée par N-064 apparaît. Elle vient d'une pièce déjà au dépôt, que les deux notes
d'antériorité de l'organisme n'ont pas lue :** Qu, Chen, Wang, « Propose, Don't Judge: An Anytime-Valid Referee for LLM
Agents That Mine Investment Factors », arXiv 2609.27051 v1, 22 septembre 2026
(`docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf`, `2a8ded0119a1…`, 37 pages).

1. **O2, énoncé retenu par N-064 : trois de ses quatre composantes sont occupées par cette pièce, sur un autre objet (des
   facteurs d'investissement tirés d'une bibliothèque finie et gelée, pas des hypothèses de recherche libres).**
   - Statistique calculée hors de l'agent, par un arbitre gelé :
     [QU p. 1] « the agent may propose, and a frozen statistical referee that the agent cannot touch must judge » ;
     [QU p. 11] « These frozen components cannot be mounted, patched or intercepted by the controller. »
   - Jugement sur des données qui n'existent pas encore quand la proposition est déposée (le principe de l'engagement
     avant les données ; sans empreinte ni sceau) :
     [QU p. 1] « The referee scores each candidate only on market outcomes revealed after submission, by betting, so its false-discovery guarantee holds at every stopping time for any proposal policy. »
   - Contrôle des comparaisons multiples entre propositions, par la procédure de Benjamini et Hochberg pour e-valeurs :
     [QU p. 2] « That rule is online e-BH, the e-value form of the Benjamini–Hochberg procedure. » ;
     [QU p. 8] « Its objective is the false-discovery rate over everything ever admitted. »
   - **Non occupée par cette pièce** : le nul formé des lois connues. Le nul de l'arbitre est « aucun avantage » :
     [QU p. 6] « The null says it has no edge: H0 : E[Xt | Gt−1 ] ≤ 0. »
   - Conséquence : de l'énoncé retenu de O2, **il ne reste comme propre, dans les pièces lues, que le nul formé des lois
     connues (O4), le sceau par empreinte, et l'objet (hypothèses de recherche libres)**. O2 n'est pas occupée en entier.
2. **O1 (« le rôle qui produit ne tient jamais la clé qui évalue ») est occupée dans son principe**, et même en entier si
   on la lit comme un principe d'architecture sans objet : c'est la thèse de la pièce, qui en revendique la priorité —
   [QU p. 2] « No prior system separates proposing from judging. » La seconde note la classait « voisine ».
3. **O20 (juge éprouvé sur vérité plantée) est occupée comme méthode** : un arbitre par e-valeurs, face à un proposeur
   modèle de langue, est éprouvé sur un monde synthétique à vérité plantée —
   [QU p. 1] « We cross three proposers (a script, a bandit and a language model) with this referee and with three deliberately leaky ones, in a synthetic world with planted truth » ;
   [QU p. 15] « Under the frozen referee, both LLM families admit 0.000 false factors per submission. »
   Les deux notes disaient déjà « pratique courante » ; seuls les chiffres propres de l'organisme restent.
4. **Aucune des trois revendications que N-064 garde comme propres (nul des lois connues O4 ; forme de l'attaque O12 ;
   banc, préenregistrement et mutations de O11) n'est trouvée occupée en entier dans les pièces lues.** Mais O11 et O12
   reçoivent un voisin plus proche (§ 2.3).

Portée de cette collision (réserves au § 7) : prépublication non relue par des pairs, une seule version, code « sur
demande » ; domaine de la finance ; hypothèses tirées d'une grille finie. Les dates de priorité de l'organisme ne sont pas
vérifiées par moi (son dépôt public est hors des chemins de mon lot).

---

## 0. Verdict en bref

- **Contre-vérification des deux notes : aucune citation ni aucune page fausse trouvée** sur O2, O11, O12, O20, O1, O4,
  O13, O17, O19 (§ 1). Un seul écart de page : la phrase de la Ladder sur l'attaque modifiée est p. 11, la note dit
  « p. 11-12 » (la phrase chevauche les deux pages ; sans effet).
- **Ce que les notes ont manqué** : le dossier `docs/sources/pdf/anteriorite-P-041-v2/c8/` (réuni pour une autre
  antériorité) contient une famille de travaux de 2025-2026 sur les portes statistiques autour d'agents qui proposent
  (§ 2). L'un d'eux porte la collision ci-dessus. Les autres resserrent O3, O9, O11, O17.
- **Références 43 et 44 d'E-valuator** : relevées (§ 3) ; **absentes du dépôt** ; non lues.
- **Nuls composites et multiplicité** (§ 4) : la multiplicité par e-valeurs pour un flux de propositions d'agent est
  occupée (Qu et al.). « Battre un nul formé des lois connues » n'est trouvé dans aucune pièce du dépôt lue ; la seule
  pièce de statistique séquentielle pure du dépôt (2208.07610) traite un autre nul composite. Zone séduisante, à durcir.
- **Travaux qui citent POPPER** (§ 5) : dix requêtes, dix-sept pistes non opposables ; aucune ne montre, d'après les
  résumés du moteur, O2 occupée en entier ; trois touchent O4 et O12 de près.

## 1. Contre-vérification des verdicts qui pèsent

Méthode : relecture des pages citées par les notes, dans le PDF empreinté ; citations recontrôlées par programme (§ 8).
Clés : POPPER = actes PMLR 267 (`docs/sources/pdf/huang-2025-icml-pmlr-267-…pdf`, `a3c4b3701543…`, 66 p.) ; EVAL =
E-valuator (`docs/sources/pdf/2512.03109v2.pdf`, `b7a46e4cf781…`, 27 p.) ; DWORK = `…/c8/1506.02629.pdf`
(`dcfbb9aa401c…`, 29 p.) ; LADDER = `…/c8/1502.04585.pdf` (`957ef4739df3…`, 16 p.) ; GAO =
`docs/sources/pdf/gao-schulman-hilton-2022-…pdf` (`c793c551a1b0…`, 28 p.) ; MIYAI = `docs/sources/pdf/miyai-2026-…pdf`
(`dbd31ea61ff8…`, 76 p.) ; NATURE et SUPPL = article et informations supplémentaires de Co-Scientist
(`docs/sources/co-scientist-v1/…`, `351f49d89d2f…`, 28 p. ; `e5595509a10d…`, 120 p.). Compagnons `.sha256` vérifiés
« OK » pour toutes les pièces de `docs/sources/pdf/` citées ici.

### 1.1 O2 — POPPER : verdict « occupée en partie » confirmé

- E-valeurs, seuil 1/α, décision hors des agents :
  [POPPER p. 3] « If the aggregated e-value exceeds 1/α, we declare sufficient evidence to reject the null hypothesis. » ;
  [POPPER p. 4] « Then, P(ŷ = 1) ≤ α under H0 ».
- La statistique vient de l'agent :
  [POPPER p. 2] « This agent ultimately produces a p-value that summarizes the outcome of the falsification experiment. » ;
  [POPPER p. 23] « The output should be a single p-value. » ;
  [POPPER p. 6] « by querying and analyzing the raw data in D to output a p-value ».
- **Précision apportée par ma lecture des pages 27 à 66, que la note n'avait lues qu'aux premières lignes.** Les
  trajectoires montrent l'étape hors de l'agent : elle reçoit la liste des p-valeurs et calcule le produit des
  e-valeurs —
  [POPPER p. 45] « List of p-values: [0.031, 0.1832, 0.028, 0.056] » ;
  [POPPER p. 45] « Summarized sequential statistics: 20.944182166241685 ».
  Mon calcul (pas un chiffre des auteurs) : ces valeurs se retrouvent avec le calibrateur κ·p^(κ−1) et κ = 0,5.
  Le code de l'agent est exécuté dans le processus du cadre, sans bac à sable visible :
  [POPPER p. 34] « exec(full_code, exec_globals) ».
- Multiplicité hors champ, comme dit par la note :
  [POPPER p. 8] « This leads to the problem of multiple hypothesis testing, which could be built upon P OPPER yet is beyond the scope of this work. » ;
  et une ouverture que la note n'avait pas relevée :
  [POPPER p. 9] « Future work can also extend P OPPER to control other error metrics beyond the Type-I error ».
  Dans une trajectoire, l'agent d'exécution corrige lui-même la multiplicité à l'intérieur d'un sous-test
  ([POPPER p. 55] « Bonferroni corrected p-value: 9.42e-02 ») : ce n'est pas un contrôle entre hypothèses.
- Revendication de priorité de POPPER, à connaître :
  [POPPER p. 15] « To the best of our knowledge, there is no work that investigates rigorous validation of a free-form hypothesis grounded with data using AI agent. »
- Réserves de la note (R4) confirmées :
  [POPPER p. 7] « remains below the nominal level across all datasets » contre 0,103 ± 0,020 au tableau 3 (p. 6) ;
  [POPPER p. 6] « operates under metadata-only access, meaning it sees only the schema of each table but has no access to raw data or summary statistics » contre
  [POPPER p. 24] « with columns and example rows ».

### 1.2 O11 et O12 — Dwork et al., Blum et Hardt : « occupées dans leur principe » confirmé

- [DWORK p. 1] « Reusing a holdout set adaptively multiple times can easily lead to overfitting to the holdout set itself. »
- [DWORK p. 21] « In this scenario no classifier can achieve true accuracy better than 50%. » ;
  [DWORK p. 21] « reusing a standard holdout results in reported accuracy of over 63% for k = 500 on both the training set and the holdout set ».
  Les cent exécutions sont bien à la page 21.
- [LADDER p. 10] « a new canonical attack that an adversarial analyst might perform in order to boost their ranking on the public leaderboard » ;
  [LADDER p. 11] « we modified the attack to be more effective against the Ladder Mechanism » ;
  [LADDER p. 10] « do not control for multiple comparisons ». Les 12 000 étiquettes dont 4 000 publiques sont p. 11 ; les
  cinq répétitions p. 12.
- [GAO p. 10] « Adversarial Goodhart occurs when the policy actively manipulates the proxy. We do not expect the effects of adversarial Goodhart to be captured in this work, as the models involved are not powerful enough to implement adversarial strategies. » ;
  [GAO p. 11] « Exploring adversarial Goodhart empirically. »
- [MIYAI p. 16] « the writing agent often responded by fabricating non-existent ablation studies in the subsequent revision, which unfortunately led to an improvement in the review score » ;
  [MIYAI p. 17] « Current AI reviewers cannot detect discrepancies between the actual experimental results and the written descriptions. »
- POPPER : [POPPER p. 16] « no signs of p-hacking were observed » ; la définition de la catégorie est bien p. 17.

### 1.3 O20, O1, O4, O13, O17, O19 — pages des notes confirmées

- O20 : [POPPER p. 7] « We assess Type-I error by creating negative examples through random column-wise permutations in each dataset, ensuring the null hypothesis holds. » ;
  [EVAL p. 8] « E-valuator empirically controls the false alarm rate across all choices of α and all datasets ».
- O1 : [POPPER p. 15] « takes in a hypothesis (generated from either LLM or human) » ;
  [NATURE p. 11] « we used Gemini 2.0 models as the base foundational LLM for all agents » ;
  [SUPPL p. 55] « final decisions are always made by scientists ».
- O4 : [NATURE p. 12] « For novelty, it summarizes known aspects of the hypothesis and then judges their novelty on the basis of existing literature » ;
  [LADDER p. 3] « it only releases a score to the participant if the score presents a statistically significant improvement over the previously best submission of the participant ».
  **Voisin manqué par la note** : dans une trajectoire, l'agent de POPPER construit de lui-même un nul de référence
  (« pas mieux qu'un gène pris au hasard ») —
  [POPPER p. 42] « GRAP2 is no more correlated with IL2 across tissues than a random gene is. » ;
  et les auteurs notent que l'agent
  [POPPER p. 8] « often includes well-chosen negative controls ».
  C'est un nul de classe de référence, posé par l'agent, pas un nul des lois connues posé par l'orchestrateur.
- O13 : [POPPER p. 6] « Without explicit prompting, it selects suitable tests » ; Co-Scientist :
  [NATURE p. 13] « the Generation agent uses this feedback selectively to avoid over-fitting to these review critiques ».
- O17 : [POPPER p. 5] « is simply recorded as a failed attempt, and the procedure moves on. » ;
  [POPPER p. 5] « Strictly speaking, ignoring the failure attempt would lead to invalid e-value if the failure event correlates with the e-value » ;
  [NATURE p. 15] « The full source code for the Co-Scientist system is not publicly available ».
- O19 : [EVAL p. 5] « the procedure never rejects (trivially controlling FAR but obtaining zero power) » ;
  [NATURE p. 14] « No statistical methods were used to predetermine sample sizes ».

### 1.4 E-valuator, lu en entier : « n'occupe aucune revendication » confirmé

- [EVAL p. 1] « a method to convert any black-box verifier score into a decision rule with provable control of false alarm rates » ;
  [EVAL p. 3] « while it guarantees control of the false alarm rate for any agent and verifier (with respect to a calibration set) » ;
  [EVAL p. 6] « applies to any scoring process with i.i.d. trajectories from the null available in the calibration set » ;
  [EVAL p. 15] « Suppose our calibration set contains n successful trajectories that are i.i.d. according to the null. »
- Recherche de termes refaite sur les 27 pages : « adversar », « goodhart », « gaming », « hack », « manipul »,
  « optimis » ou « optimiz » : zéro occurrence. Rien sur un agent qui s'adapte au surveillant ; rien sur la
  multiplicité entre hypothèses ; rien sur un nul de lois connues.
- Suite annoncée, qui touche le programme de contrôle lui-même (déjà signalée par la note) :
  [EVAL p. 10] « such as early detection of unsafe or harmful trajectories ».

## 2. Ce que les notes ont manqué, dans les pièces du dépôt

Toutes ces pièces sont sous `docs/sources/pdf/anteriorite-P-041-v2/c8/` sauf mention. Étendue de ma lecture au § 7.

### 2.1 Qu, Chen, Wang (arXiv 2609.27051 v1, 22 septembre 2026) — clé QU

- Identité : [QU p. 1] « arXiv:2609.27051v1 [cs.AI] 22 Sep 2026 ».
- Thèse et mécanisme : voir le bloc COLLISION. Appuis théoriques cités, que l'article dit appliquer sans les étendre :
  [QU p. 4] « The e-BH procedure (Wang and Ramdas 2022) and its online form (Fischer et al. 2024; Wang et al. 2025; Heide 2026) control the false-discovery rate over a growing set at data-dependent stopping times. »
- Hypothèse unique de la garantie :
  [QU p. 2] « They rely on one hypothesis: the proposer has no information about the post-submission stream. » ;
  elle tombe en rejeu historique : [QU p. 14] « A language model trained on the campaign years falls outside condition (iv) of Proposition 1. »
- Univers d'hypothèses fini et gelé : [QU p. 30] « The library is fixed in advance, keeping the hypothesis universe finite ».
- Menace nommée, proche de O12 :
  [QU p. 6] « Verifier-in-the-loop adaptation means that the controller learns what the referee rewards. » ;
  [QU p. 18] « The guarantee also holds for a proposer that adapts to the verdicts. »
- Attaquant scripté, proche de O11 :
  [QU p. 16] « An attacking controller extracts false admissions only from a leaky referee. Hidden retries resubmit unadmitted candidates under new identifiers rather than drawing fresh ones. »
- Monde planté : [QU p. 14] « The synthetic world isolates the mechanism, because truth is planted. It has four families with true-factor proportions 0.50/0.25/0.10/0.05 » — donc **pas** un monde où toute promotion est fausse.
- Coût de la garantie, proche de O19 : [QU p. 9] « A factor whose edge sits at δ needs more than five years of evidence. »
- Garde éprouvée sur un artefact, journal en ajout seul, plan préenregistré avec amendements datés (voisins de O17) :
  [QU p. 11] « A unit test reproduces the counterexample and confirms that the invariant removes it. » ;
  [QU p. 5] « Decision Log (Append-Only) » ;
  [QU p. 36] « Dated amendments to the pre-registered design. »
- Ce que la pièce situe comme antérieur à elle : les portes à validité permanente autour d'agents qui se modifient —
  [QU p. 4] « Both certify the agent’s own modifications. » (SEA et PACE, § 2.2).
- **Ce que la pièce ne fait pas, d'après ma lecture** : aucun nul formé de facteurs connus ; aucune empreinte ni sceau de
  la proposition ; aucun proposeur à qui l'on donne la description exacte de l'arbitre avec la consigne de le tromper ;
  aucun monde tout faux ; aucune hypothèse libre. L'attaquant est un script ; le proposeur modèle de langue alloue des
  soumissions entre familles et écrit des sondes de diagnostic.

### 2.2 Portes statistiques autour d'agents qui se modifient (objet différent : les modifications de l'agent)

- PACE (arXiv 2606.08106 v1, `779f49607688…`, 12 p.) :
  [PACE p. 1] « The agent effectively p-hacks itself » ;
  [PACE p. 1] « committed only when a testing-by-betting e-process accumulates decisive evidence » ;
  un positif planté parmi les propositions (voisin de O10) :
  [PACE p. 1] « With a known beneficial edit hidden among noisy proposals ».
- SEA (arXiv 2607.00871 v1, `fb50bba836f7…`, 30 p.) :
  [SEA p. 1] « admits each modification only through an anytime-valid gate that emits an auditable certificate against a fixed error budget ».
- Statistical Gödel Machines (arXiv 2510.10232 v2, `ad17c77e8f5f…`, 25 p.) :
  [SGM p. 1] « SGM separates adaptive proposal generation from confirmation » ;
  [SGM p. 1] « without guaranteeing that improvements will be found ».
- REUSE (arXiv 2609.33180 v2, `20639707e89e…`, 41 p.) — limiter le retour de l'évaluation vers la recherche (O9) :
  [REUSE p. 1] « strictly limiting the evaluation feedback returned to the search process » ;
  [REUSE p. 1] « reducing the proportion of promotions that are false from up to 20.7% to 0% ».
- SEAL (arXiv 2607.24300 v1, `0a1434ea1c9b…`, 9 p.) — audit scellé, retour réduit à un bit (O1, O9) :
  [SEAL p. 1] « The agent cannot author or inspect the audit, receives only accept/reject ».
- PROCTOR (arXiv 2609.02246 v1, `9a2923ab0007…`, 20 p.) — couche déterministe au-dessus du juge modèle (O13, O17, O18) :
  [PROCTOR p. 1] « every change is gated instead by a deterministic verification layer that the judge has no power to override » ;
  [PROCTOR p. 1] « Agents achieved perfect scores by reading cached answer keys from their environment » ;
  un repli silencieux observé :
  [PROCTOR p. 1] « A syntactically broken prompt was promoted as the winning candidate because a silent parser fallback improved the metric. »

### 2.3 Attaques adaptatives contre un audit réutilisé (O11, O12)

- Mittal et Gupta, « Signed Compression Progress on a Sealed Audit is Goodhart-Resistant » (arXiv 2606.11417 v1,
  `7ae148beb5c7…`, 16 p.) — clé AUDIT :
  [AUDIT p. 1] « naive reusable audits are exploitable by black-box scalar feedback, while fresh subsampling, laddering, rounding, and one-shot release keep the attack below the 2∆n threshold » ;
  [AUDIT p. 9] « the attacker sees only released audit scores » ;
  [AUDIT p. 10] « Naive reuse is exploitable in all 20 seeds ».
  Attaquant scripté, par le seul retour scalaire, contre un audit dit « scellé », avec les défenses de 2015 rejouées.
  Même principe que O11 et O12 ; pas de proposeur modèle de langue, pas de juge statistique d'hypothèses.

### 2.4 The Agentic Scientist (`docs/sources/pdf/2610.18933v1.pdf`, `cb170b543574…`, 88 p.) — clé AGSCI

Citée par la première note (§ 7, point 7) comme « évaluateur et grille scellés », non lue par elle. Lue ici par recherche
de termes seulement.
- [AGSCI p. 6] « An independent audit agent runs every round on a read-only copy of the workspace » : l'audit est un
  agent modèle, pas une règle statistique.
- [AGSCI p. 22] « AI reviewer scores can potentially be overfit like any other metric » ; piste pour O7 :
  [AGSCI p. 22] « Reviewers drawn from several model families ».
- Empreintes liant poids, configuration et évaluateur (voisin de O17) :
  [AGSCI p. 45] « The selected weights are serialized, hashed, and re-loaded under a runtime identity check that binds the source hash, the configuration digest, and the evaluator hash. »
- Je n'y ai trouvé ni e-valeur, ni contrôle de multiplicité, ni le mot « preregist » (termes cherchés sur les 88 pages) ;
  une consigne de tâche y demande des points de contrôle déclarés d'avance (p. 74), sans règle statistique.

## 3. Références 43 et 44 d'E-valuator

- Relevé, dans la liste des références :
  [EVAL p. 13] « [43] Can Chen and Jun-Kun Wang. Online detection of llm-generated texts via sequential hypothesis testing by betting. In International Conference on Machine Learning, pages 9231–9276. PMLR, 2025. » ;
  [EVAL p. 13] « [44] Guneet S. Dhillon, Javier Gonzalez, Teodora Pandeva, and Alicia Curth. E-scores for (in)correctness assessment of generative model outputs. In The 29th International Conference on Artificial Intelligence and Statistics, 2026. »
- Pourquoi E-valuator les cite : une seule fois, dans les travaux voisins, comme exemples d'usage des e-valeurs, à côté
  de POPPER (référence 8) —
  [EVAL p. 6] « They have found applications in many settings, including A/B testing [40], changepoint detection [41, 42], and others [43, 8, 44]. »
  Rien d'autre n'en est dit.
- **Au dépôt : non.** Vérifié sur disque (R11) : `ls` de `docs/sources/pdf/` et de ses sous-dossiers
  `anteriorite-P-041-v1`, `anteriorite-P-041-v2/c1` à `c8`, `complement-1` à `4`, `refutation-1` et `2`,
  `bisociation-fertilite-v1`, `bisociation-litterature-reelle-v1`, `demande-conv-audit-2026-10-31-v1`,
  `identification-causale-v1` ; plus un index des premières lignes de la première page des 626 PDF de ces dossiers
  (527 + 99), cherché sur « betting », « e-score », « e-value ». Aucun des deux titres.
- **Donc non lues contre O2, O4, O11, O12, O19.** D'après leurs seuls titres (non opposable) : la 43 détecte des textes
  produits par modèle par un test séquentiel par pari ; la 44 note la justesse de sorties de modèles génératifs. Ni l'une
  ni l'autre ne paraît porter sur des hypothèses de recherche ; la 44 est la plus proche de O2 (e-valeurs pour juger des
  sorties de modèle). À récupérer (§ 9).

## 4. Nuls composites par e-valeurs et multiplicité : qui occupe quoi, dans le dépôt

### 4.1 « Contrôle des comparaisons multiples » (O2)

- **Occupé, pour un flux de propositions d'agent jugées par e-valeurs : Qu et al.** (e-BH en ligne, [QU p. 2], [QU p. 8],
  appuis [QU p. 4], cités au § 2.1 et au bloc COLLISION).
- POPPER le laisse hors champ ([POPPER p. 8], § 1.1). E-valuator n'en parle pas. La Ladder dit ne pas le faire
  ([LADDER p. 10], § 1.2). PACE donne une garantie par décision, pas par course (résumé, p. 1).
- La pièce de statistique du dépôt signale l'usage des e-valeurs en tests multiples, sans le traiter :
  [ESTAT p. 2] « for example in multiple testing (Wang and Ramdas, 2022; Ren and Barber, 2022) ».
- La procédure elle-même (Wang et Ramdas 2022) n'est pas au dépôt : c'est l'outil standard, à citer, pas à revendiquer.

### 4.2 « Battre un nul formé des lois connues » (O4)

- **Non trouvé dans les pièces lues.** Les nuls rencontrés : nul de chaque sous-test posé par l'agent (POPPER, p. 4, 24) ;
  nul de classe de référence posé par l'agent ([POPPER p. 42]) ; nul « aucun avantage » ([QU p. 6]) ; nul « la
  trajectoire réussira » (E-valuator, p. 3) ; « battre le meilleur précédent d'une marge » ([LADDER p. 3]) ; « le candidat
  ne fait pas mieux que le titulaire » (PACE, SGM, REUSE, résumés p. 1).
- La seule pièce de statistique séquentielle pure du dépôt, Pérez-Ortiz, Lardy, de Heide, Grünwald, « E-statistics,
  group invariance and anytime-valid testing » (`docs/sources/pdf/2208.07610v2.pdf`, `e9e5fd4e0096…`, 31 p., clé ESTAT),
  traite un **autre** nul composite : celui qui est invariant sous un groupe de transformations —
  [ESTAT p. 1] « We develop e-statistics and anytime-valid methods (Ramdas et al., 2023) for composite hypothesis testing problems where both null and alternative models remain unchanged under a group of transformations. »
  Elle n'occupe pas O4 ; elle montre que le nul composite par e-valeurs est un domaine établi de la statistique.
- E-valuator nomme l'outil général, sans l'employer :
  [EVAL p. 10] « which would allow universal inference algorithms [74] to construct exact e-processes from estimated density ratios ».
- **Réserve (R8), forte.** O4 est la zone la plus séduisante qui reste : c'est donc celle à vérifier le plus durement.
  « Un nouveau prédicteur doit ajouter quelque chose aux prédicteurs connus » est, de mémoire et non vérifié, une
  pratique ancienne de la finance empirique (tests d'englobement d'un facteur par les facteurs connus) et de la
  comparaison séquentielle de prévisionnistes. Trois pistes du § 5 la touchent. « Libre dans les pièces lues » ne dit
  rien de plus.

### 4.3 Titres à récupérer, relevés dans les bibliographies

- **POPPER** (p. 10 à 13) : Vovk et Wang, [POPPER p. 12] « E-values: Calibration, combination and applications. » ;
  Grünwald, de Heide, Koolen, [POPPER p. 10] « Safe testing. » ; Shafer,
  [POPPER p. 12] « The language of betting as a strategy for statistical and scientific communication. » ; Li et al.,
  [POPPER p. 11] « Critical: Critic automation with language models. » (voisin déclaré : tests d'hypothèses conduits par
  modèle pour critiquer des modèles statistiques, p. 15).
- **E-valuator** (p. 11 à 15) : [EVAL p. 11] « [18] Aaditya Ramdas and Ruodu Wang. Hypothesis testing with e-values. » ;
  Vovk et Wang, [EVAL p. 12] « Confidence and discoveries with e-values. » ;
  [EVAL p. 12] « Peter Grünwald, Rianne de Heide, and Wouter M Koolen. Safe testing. » ; Wasserman, Ramdas, Balakrishnan,
  [EVAL p. 15] « Universal inference. » ; les références 43 et 44 (§ 3).
- **Qu et al.** (cités p. 4, liste p. 22 à 24) : Wang et Ramdas 2022 (e-BH) ; Fischer et al. 2024 et Wang et al. 2025
  (e-BH en ligne, arrêté) ; Heide 2026 (« dynamic e-closure ») ; Waudby-Smith et Ramdas 2024 (pari pour moyennes
  bornées) ; Harvey et al. 2016 et Bailey et López de Prado 2014 (multiplicité en recherche de facteurs).

## 5. Travaux qui citent POPPER ou reprennent ses idées — PISTES, non opposables

Dix requêtes de l'outil de recherche sur le réseau, le 10 novembre 2026, sans nom de directeur, de projet, de dépôt ni de
fonds. Tout ce qui suit vient des résumés du moteur : **piste, non vérifiée**. Le moteur n'a rendu aucune liste des
travaux qui citent POPPER ; « non trouvé en dix requêtes » ne veut pas dire « n'existe pas ».

| n° | piste (titre, auteurs, identifiant, date) | ce que le résumé du moteur en dit | axe | revendication | priorité |
|---|---|---|---|---|---|
| 1 | Xu, Fischer, Ramdas, « Improving online FDR procedures via online analogs of e-closure and compound e-values », arXiv 2603.24792, 25 mars 2026 ; PMLR 337:7552-7561 | contrôle en ligne du taux de fausses découvertes par e-valeurs ; l'introduction poserait le cas d'hypothèses produites en séquence par un scientifique « ou un agent modèle de langue » | (c) | O2 | haute |
| 2 | Jin, « Popper handout », `ying531.github.io/assets/files/Popper_handout.pdf`, non daté | les auteurs de POPPER proposeraient d'étendre par e-BH à plusieurs hypothèses | (c) | O2 | haute (court) |
| 3 | Asher et al., 2026, identifiant inconnu | agents de code lancés sur les données de quatre articles à résultats nuls connus ; une consigne qui déguise la recherche de significativité | (b) | O11, O12 | **haute** : proche de la forme « proposeur modèle sur monde nul » |
| 4 | « Mitigating LLM-based p-Hacking by Preregistering for the Next LLM », arXiv 2606.27687, 2026 | le préenregistrement classique ne protège pas les analyses par modèle ; préenregistrer contre le prochain modèle | (a), (b) | O3, O12 | haute |
| 5 | Billet de forum « Measuring how often an AI research agent fools itself » (protocole « SDCP »), forum.effectivealtruism.org, 2026 | hypothèses, seuils et plans gelés et empreintés avant les données ; générateur et évaluateur séparés ; seul l'évaluateur ouvre les résultats scellés | (a) | O1, O3, O17 | haute (pas un article) |
| 6 | Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, 2026 | modèle de langue dans un cadre contraint ; tests de nouveauté par englobement contre 209 anomalies publiées ; 280 propositions, quelques survivantes | (c) | **O4** | **haute** |
| 7 | Pan, Ding, Giesecke, « Agentic Empirical Asset Pricing: Methodological Foundations », arXiv 2609.00731, 2026 | norme d'évaluation des facteurs trouvés par agents | (a), (c) | O2, O4 | moyenne à haute |
| 8 | Choe et Ramdas, « Comparing Sequential Forecasters », arXiv 2110.00115 | e-processus pour le nul composite « un prévisionniste ne fait pas mieux que l'autre en moyenne » | (c) | O4 | haute (déjà listée par les notes) |
| 9 | Henzi et Ziegel, « Valid sequential inference on probability forecast performance », arXiv 2103.08402 | test de dominance de prévisions par e-valeurs, valide sous arrêt optionnel | (c) | O4 | haute (déjà listée) |
| 10 | Miao, Pritchard, Zou, « The Agentic Garden of Forking Paths », arXiv 2607.01507, juillet 2026 | « m-valeur » : part des chemins d'analyse d'agents qui donneraient un résultat aussi extrême ; « Agentic Bootstrap » | (a) | O2, O13 | moyenne |
| 11 | « Preregistration for Experiments with AI Agents », arXiv 2606.11217, 2026 | gabarit de préenregistrement pour expériences avec agents ; verrou des versions de l'évaluateur | (a) | O3, O17 | moyenne |
| 12 | « When Do Agent Loops Mistake Stagnation for Progress? … », arXiv 2607.25152, 2026 | séparation du générateur et d'un évaluateur ancré dans une vérité externe ; gel par empreinte prescrit mais non achevé | (a) | O1, O3 | moyenne |
| 13 | Xu et Ramdas, contrôle en ligne du taux de fausses découvertes par e-valeurs, PMLR 238, 2024 | fondement du contrôle en ligne sous dépendance inconnue | (c) | O2 | moyenne |
| 14 | « Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation », arXiv 2608.01666, 2026 | les juges modèles d'idées de recherche suivent le style, pas le fond | (b) | O18 | moyenne |
| 15 | « Large Language Model Hacking », arXiv 2509.08825, 2025 | conclusions faussées par des annotations de modèle dans 31 à 50 % des cas | (b) | O11 | basse |
| 16 | arXiv 2607.17409, juillet 2026, titre non relevé | évaluation séquentielle d'un nouveau modèle par produit d'e-valeurs conditionnelles | (c) | O2 | basse |
| 17 | Lindon, « Anytime-valid testing in the age of AI-assisted software development », ERCIM News 145 | tests à validité permanente pour le développement assisté | (a) | O2 | basse |

Lecture d'ensemble, non opposable : sur l'axe (a), les résumés montrent du gel par empreinte et de la séparation des
rôles (pistes 5, 11, 12), mais pas la combinaison « e-valeurs + nul des lois connues + sceau » ; sur l'axe (b), la piste 3
est celle qui peut occuper la forme de O12 ; sur l'axe (c), la pièce du dépôt (Qu et al.) occupe déjà plus que toutes les
pistes.

## 6. Table finale O1 à O20

Statuts de la consigne du lot. « Avant » : colonne « après » de la table § 7 de la seconde note, et N-064. Les pages de Qu
et al. et des autres pièces de c8 sont citées aux § 2 et au bloc COLLISION.

| | revendication (abrégée) | avant | verdict de ce rapport | changement |
|---|---|---|---|---|
| O1 | le rôle qui produit ne tient jamais la clé qui évalue | voisine | **occupée dans son principe** (Qu et al., p. 1, 2, 11 ; aussi SGM p. 1, SEAL p. 1, pour des modifications d'agent) | **oui** |
| O2 | statistique calculée par l'orchestrateur, engagement scellé avant les données, nul des lois connues, multiplicité contrôlée (énoncé de N-064) | occupée en partie (POPPER, p. 2-5, 14) | **occupée en partie, plus largement** : e-valeurs et seuil (POPPER, p. 3-5, 14) ; statistique hors de l'agent, jugement sur données postérieures au dépôt, e-BH (Qu et al., p. 1, 2, 8, 11) ; restent le nul des lois connues, le sceau par empreinte, l'objet | **oui** (COLLISION) |
| O3 | prédictions scellées avant les données ; tirages semés par l'empreinte | voisine | **occupée dans son principe** pour « jugé seulement sur des données postérieures au dépôt » (Qu et al., p. 1, 2, 10) ; sceau par empreinte et tirages semés non trouvés | **oui** |
| O4 | battre un nul des lois connues | non occupée (une voisine) | **libre dans les pièces lues** ; voisines : Ladder p. 3, POPPER p. 42, 2208.07610 p. 1 ; zone à durcir (§ 4.2, pistes 6 à 9) | non (réserve renforcée) |
| O5 | moisson bibliographique non opposable ; trou = question | occupée dans son principe | inchangée (non réexaminée) | non |
| O6 | douane de forme, coffre scellé | voisine | inchangée (non réexaminée) | non |
| O7 | juges croisés de plusieurs fournisseurs | voisine | voisine (The Agentic Scientist p. 22, comme suite souhaitée) | non |
| O8 | proposeurs de plusieurs fournisseurs | non occupée | libre dans les pièces lues ; voisine : Qu et al. croisent des familles de modèles sans les mêler (p. 2, 14) | non |
| O9 | mémoire sans verdicts ni témoins ; juges aveugles aux notes | voisine | **occupée dans son principe** pour « limiter le retour du juge vers le proposeur » (Dwork p. 3 ; REUSE p. 1 ; SEAL p. 1) ; la forme « aucun verdict » non trouvée ; choix contraire chez Qu et al. (p. 5, 18) | **oui**, confiance moyenne |
| O10 | témoins plantés mêlés à chaque génération | voisine | voisine (PACE p. 1 : positif planté parmi les propositions ; Qu et al. p. 14) | non |
| O11 | banc de tricheurs scriptés ; validation préenregistrée ; mutations | occupée dans son principe | **occupée dans son principe**, voisins plus proches : attaquant scripté contre un arbitre par e-valeurs (Qu et al., p. 16), attaque et défenses rejouées (2606.11417, p. 1, 9, 10) ; banc de 27, préenregistrement, mutations non trouvés | non (resserrée) |
| O12 | attaque de Goodhart : proposeur modèle qui lit le juge et ses verdicts, mondes tout faux | occupée dans son principe ; forme non trouvée | **occupée dans son principe** ; voisin plus proche : proposeur modèle qui reçoit les verdicts d'un arbitre statistique sur monde planté (Qu et al., p. 6, 14, 15, 18) ; **la forme (description exacte du juge, mondes tout faux, attaque voulue) reste non trouvée dans les pièces lues** ; piste 3 à lire | non (resserrée) |
| O13 | tests de mort en bac à sable, verdict de l'orchestrateur sur le fichier brut | voisine | voisine (POPPER p. 6, 23, 34 ; PROCTOR p. 1 ; The Agentic Scientist p. 6) | non |
| O14 | sélection entre générations par le verdict des tests de mort | voisine | voisine (PACE, SGM, REUSE p. 1 : ne garder une modification que sur porte statistique) | non |
| O15 | bisociateur à trois bras | voisine | inchangée (non réexaminée) | non |
| O16 | pont fiche → loi prédictive | voisine | voisine (POPPER p. 2, 4, 24) | non |
| O17 | scellement avant lecture ; aucun repli silencieux ; mutations | non occupée | **voisine** (Qu et al. p. 5, 11, 36 ; PROCTOR p. 1 ; The Agentic Scientist p. 45) ; le banc de mutations et la règle « aucun repli silencieux » non trouvés | **oui** |
| O18 | discrimination des juges modèles mesurée | voisine | voisine (POPPER p. 8, 18 ; PROCTOR p. 1) | non |
| O19 | puissance du juge mesurée ; « rien promu » ≠ absence d'effet | voisine | voisine (POPPER p. 6, 9 ; E-valuator p. 5, 8 ; Qu et al. p. 9 ; SGM p. 1) ; lecture d'un « rien promu » comme borne d'effet non trouvée | non |
| O20 | juge éprouvé sur vérité plantée | occupée dans son principe (pratique courante) | **occupée comme méthode** (POPPER p. 7 ; Qu et al. p. 1, 14, 15) ; restent les chiffres propres | **oui** (COLLISION, point 3) |

**Par rapport à N-064.** Point 2 (O2) : l'énoncé retenu ne suffit plus à séparer l'organisme des pièces lues ; trois de ses
quatre composantes sont occupées par Qu et al. Point 3 (O11, O12) : tient, avec un voisin de plus à citer. Point 4
(citations obligatoires) : Qu et al. devrait rejoindre la liste, et sans doute REUSE et PACE. **Je ne modifie rien : c'est
un nœud de Lazar (zone revendiquée trouvée occupée plus largement ; modification de revendication).**

**Phrase honnête à dire à un jury.** « Séparer celui qui propose de celui qui juge, juger par e-valeurs avec contrôle des
comparaisons multiples sur des données postérieures à la proposition, et éprouver ce juge sur un monde à vérité plantée :
tout cela existe déjà (POPPER, 2025 ; Qu, Chen et Wang, septembre 2026, pour des facteurs d'investissement) ; ce que
l'organisme apporte, et que je n'ai trouvé dans aucune pièce lue, c'est un juge dont le nul est formé des lois déjà
connues, appliqué à des hypothèses de recherche libres, et la mesure de ce juge sous l'attaque d'un proposeur modèle de
langue qui en lit la règle sur des mondes où toute promotion est fausse — et cette dernière affirmation vaut pour les pièces
lues, pas pour le champ. »

## 7. Réserves

- **Symétrie (R4), sur ma trouvaille.** Qu et al. : prépublication, une version, non relue par des pairs ; auteurs de deux
  sociétés ; [QU p. 22] « The code, run manifests, prompts, and recorded model calls are available from the corresponding author on request ».
  Le « 0,000 » de fausses admissions repose sur cinq graines et deux familles de modèles (tableau 8, p. 29). Sur données
  réelles, l'étiquette favorise l'arbitre gelé, de l'aveu des auteurs : [QU p. 22] « The registered label leans towards the frozen referee. »
  Rapporté comme dit, jamais comme établi. La collision porte sur le **mécanisme décrit**, pas sur la solidité des
  résultats.
- **Identité de la pièce.** Je n'ai pas lu la provenance du dossier c8 (hors de mon lot) ; l'identifiant et la date sont
  ceux imprimés en page 1 ; le compagnon `.sha256` est « OK ». À recouper avec la page arXiv avant tout usage opposable
  de la date.
- **Symétrie, sur la contre-vérification.** Zéro échec sur les citations des notes est un résultat propre : il tient en
  partie à ce que je contrôle les mêmes extractions `pdftotext` que les notes. Aucune figure relue en image.
- **Étendue de ma lecture.** POPPER : p. 1 à 9 et 14 à 26 en entier ; p. 10 à 13 (références) par recherche ; p. 27 à 46
  sur les 2 600 premiers caractères de chaque page et p. 47 à 66 sur les 900 premiers, plus une recherche de termes sur
  les 66 pages (trajectoires d'exemple) : **pas « en entier » au sens strict pour les pages 27 à 66**. E-valuator : en
  entier (p. 16 à 27 : lignes de prose, tableaux et figures non relus). Qu et al. : p. 1 à 11 en entier ; p. 12 à 16, 18,
  21, 22, 25 en lignes de prose ; le reste par recherche de termes ; preuves et tableaux d'annexe non relus. PACE, SEA,
  SGM, REUSE, SEAL, PROCTOR, 2606.11417 : page 1 et recherche de termes. The Agentic Scientist : recherche de termes.
  2208.07610 : p. 1 à 3. Dwork, Ladder, Gao, Miyai, Co-Scientist : pages citées par les notes seulement.
- **Pièces de c8 non ouvertes** qui touchent peut-être O11, O12, O14, O18 (titres relevés en page 1 seulement) :
  2610.09239 (« The Winner's Curse in LLM Self-Improvement Loops », étude préenregistrée), 2607.12790 (« Who Grades the
  Grader? »), 2609.00652 (« Self-Reports Are Not Verification »), 2610.27610, 2610.38392, 2610.14216, 2609.17560.
- **O5, O6, O15** non réexaminées (hors des verdicts « qui pèsent » de la consigne). **O9** : changement de statut à
  confiance moyenne (la forme « aucun verdict » est plus stricte que tout ce qui est lu).
- **Recherche sur le réseau** : dix requêtes, moteur généraliste, résumés non vérifiés, identifiants non recoupés.
- Aucun refus de permission rencontré.

## 8. Contrôle des citations

Script `controle_citations.py`, gardé dans
`/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotC4/` (non versé). Il
relève dans ce rapport chaque motif « [CLÉ p. N] « citation » » et cherche la citation dans le texte de la page N du PDF
de la clé (`pdftotext`, ordre de lecture puis `-layout` ; Unicode normalisé, apostrophes et guillemets ramenés à leur forme
simple, césures de fin de ligne recollées, blancs réduits). Essai préalable (R5) : cas juste retrouvé ; cas altéré (un mot
changé) en échec ; bonne citation à la mauvaise page en échec. Résultat sur ce rapport : voir le § 8 bis, écrit après la
dernière passe et avant le scellement. Les mentions de page sans guillemets (« p. 14 », « p. 29 ») ne sont pas des
citations exactes et ne sont pas contrôlées par programme ; les chiffres qu'elles portent sont lus dans le texte extrait.

### 8 bis. Résultat

Contrôle lancé à 10:58 UTC puis relancé après la dernière retouche (10:59 UTC, `date -u`) : **105 citations contrôlées,
105 retrouvées à la page citée, 0 échec.** Avant l'écriture, 121 citations candidates avaient été contrôlées (dont celles
des deux notes pour les verdicts qui pèsent) : 120 retrouvées, 1 échec, expliqué — la phrase de la Ladder « we modified
the attack… » est à la page 11 et non 12 (elle finit en bas de la page 11) ; ce rapport la cite p. 11.

## 9. Pièces à récupérer sur le réseau, par ordre

1. **Asher et al. 2026** (identifiant à trouver) — agents de code sur données à résultats nuls connus : peut occuper la
   forme de O12.
2. **Liu, Liu, Liu, Mei, SSRN 6569258** et **Pan, Ding, Giesecke, arXiv 2609.00731** — nouveauté jugée contre les
   prédicteurs connus : O4.
3. **Choe et Ramdas, arXiv 2110.00115 ; Henzi et Ziegel, arXiv 2103.08402** — nul composite « ne fait pas mieux que » : O4.
4. **Wang et Ramdas 2022 (e-BH, arXiv 2009.02824 selon la première note) ; Xu, Fischer, Ramdas, arXiv 2603.24792 ;
   Fischer et al. 2024 ; Heide 2026** — multiplicité par e-valeurs, appuis de Qu et al. : O2.
5. **Références 43 et 44 d'E-valuator** (Chen et Wang, actes PMLR 2025, p. 9231-9276 ; Dhillon et al., AISTATS 2026) : O2.
6. **« Popper handout » de Jin** et **le code public de POPPER** (lecture de la p-valeur dans la sortie de l'agent) : O2.
7. **arXiv 2606.27687 ; arXiv 2606.11217 ; le billet « SDCP »** — gel par empreinte, préenregistrement d'agents : O3, O17.
8. **Wasserman, Ramdas, Balakrishnan 2020 ; Grünwald, de Heide, Koolen ; Ramdas et Wang 2025 ; Vovk et Wang 2021** —
   fondements à citer : O2, O4.
9. **Page arXiv de 2609.27051** (versions, date) et, si elle existe, une version publiée : pour dater la collision.

Version 1 ; jamais réécrite (R12).
