# Lecture entière de BEYOND (Huang et Fan, arXiv 2603.14288 v2) contre O4 — v1

- **Lecteur : modèle I.** Pièce voisine de la revendication O4 (juge au nul formé des lois connues) de l'organisme d'idéation. Verdict en vigueur sur O4 : **occupée en partie** (note d'englobement v3, section 0). Cette lecture ne le modifie pas ; tout écart ou toute précision est un nœud pour Lazar (section 8).
- **Heures (`date -u`, recopiées)** : début de lecture 2026-11-18T01:53:42Z (empreinte du PDF recalculée, commit du clone relevé) ; extraction des 60 pages 2026-11-18T01:53:59Z ; relevé du code 2026-11-18T01:56:10Z ; rejeu des citations 2026-11-18T01:58:33Z ; rejeu final des extraits de code 2026-11-18T01:59:35Z.
- **PDF** : `docs/sources/pdf/lecture-o4-v1/arxiv-2603.14288/2603.14288v2.pdf`, 60 pages (`pdfinfo`), sha256 `8fe2b21770af074a0e13667048bc40b3eb85fc03ecde8f5d58938e3aa100e301`, recalculé ce jour, conforme.
- **Code** : clone en lecture seule `code-o4/agentic-factor-investing` (dossier de travail de la session), origine `https://github.com/allenh16/agentic-factor-investing`, commit `cc8bd7d06c26f39dc379157208482fe0da19623e` (`git rev-parse HEAD`, conforme) ; clone superficiel (un seul commit visible, `git rev-parse --is-shallow-repository` : vrai). Provenance : `docs/sources/code/lecture-o4-v1/beyond/provenance-v1.md`.
- **Profondeur** : PDF lu **en entier**, 60 pages sur 60, page par page (`pdftotext -layout -f N -l N`), annexes et bibliographie comprises ; figures non lues comme images (section 1). Code : les trois fichiers textuels du dépôt lus en entier ; l'image non lue.
- **Rejeu** : citations PDF **61 sur 61** (`lecture-entiere-beyond-o4-v1-resultat-citations-pdf.json`, programme `verifier_citations_priorite_haute_o4_v1.py` inchangé) ; extraits de code **14 sur 14** (`lecture-entiere-beyond-o4-v1-resultat-extraits-code.json`, programme `verifier_extraits_code_o4_v1.py` inchangé). Contrôle supplémentaire, hors dépôt, plus strict que le programme de citations (espaces réduits, casse et ponctuation gardées) : 59 sur 61 ; les deux écarts sont des césures de fin de ligne que `pdftotext` sans `-layout` recolle sans trait d'union (p. 1, `out-ofsample` ; p. 35, `multiobjective`), alors que la mise en page montre `out-of-` et `multi-` en fin de ligne ; j'ai gardé le mot avec son trait d'union, tel qu'il s'écrit ailleurs sur les mêmes pages.
- **Règles** : R7 (rien sans page ni lignes), R8 (non trouvé = non trouvé dans ce qui est lu, à la profondeur déclarée), R4 (en cas de doute, sens non flatteur pour notre revendication), N-067 (personne ici ne déclare O4 libre). Les guillemets français de cette note ne servent qu'aux citations, toutes dans l'un des deux fichiers de rejeu.

## 1. Profondeurs

| objet | lu en entier | lu en partie | non lu, avec la raison |
|---|---|---|---|
| PDF, texte | p. 1 à 60 (résumé, introduction, littérature, méthode, données, résultats, section 6 sur l'exploration abusive des données, robustesse, conclusion, remerciements, disponibilité des données, bibliographie p. 48-51, annexes A à D p. 52-60) | — | aucune page sautée |
| PDF, figures | légendes lues | — | contenu graphique des exhibits 1 (p. 3), 2 (p. 17), 4 (p. 19), 11 (p. 29), 12 (p. 30), 14 (p. 32), 17 (p. 42), 19 (p. 44), 20 à 22 (p. 58-60) : images, non lisibles par `pdftotext` |
| PDF, tables tournées | p. 24 (exhibit 7) et p. 41 (exhibit 16) lues en mode mise en page | — | — |
| Code | `README.md` (1 ligne), `chart_data.json` (1 ligne, 502 points, structure et premier et dernier points relevés par lecture JSON), `index.html` (507 lignes) | — | `project-framework.png` (image) |

Le dépôt ne contient **pas de code du système** (section 4). Les références citées par l'article (Harvey et Liu 2021 pour la mesure d'ordonnée à l'origine réduite, López de Prado 2018, Harvey, Liu, Zhu 2016) ne sont pas lues.

## 2. Recherche de termes

Recherche insensible à la casse sur le texte de chaque page (`pdftotext -layout`, lignes jointes, césures recollées) ; le nombre entre parenthèses est le nombre d'occurrences sur la page.

| terme | résultat |
|---|---|
| `e-value`, `e-process`, `anytime`, `martingale`, `optional stopping`, `stopping`, `sequential test` | aucune occurrence |
| `sequential` | p. 1, 17, 18, 33, 52, 55 : sens courant (prise de consignes successives, apprentissage séquentiel, sélection successive des échantillons, arbres successifs) ; aucun test séquentiel |
| `likelihood ratio`, `Bayes factor` | aucune occurrence |
| `likelihood` | p. 34 (vraisemblance de découvrir un motif fallacieux, au sens courant), p. 53 (les lois du cadre conceptuel ne sont pas estimées par maximum de vraisemblance) |
| `Bayes` | p. 34 : la justification économique agit comme un a priori bayésien (image, aucun calcul) |
| `encompass`, `spanning` | aucune occurrence |
| `spanned` | p. 45 et p. 55 : alphas non expliqués par les modèles de facteurs, mesurés a posteriori |
| `incremental` | p. 4, 21, 22, 26, 44 : valeur ajoutée de la combinaison ou du pipeline ; p. 34 : pouvoir explicatif incrémental sur les références établies, affirmé |
| `marginal` | p. 35 (deux fois : information marginale sur le modèle à cinq facteurs) ; p. 39 (impact marginal sur les prix, sens économique) |
| `benchmark` | p. 4, 19, 20, 21, 26, 29, 34, 35, 43, 44, 50, 58-60 : modèle de référence de combinaison, modèles de facteurs, cadre classique d'extraction de facteurs, ligne zéro des figures |
| `baseline` | p. 18, 19, 21 : échantillon, jeu de prédicteurs, référence d'un facteur seul |
| `null` | aucune occurrence |
| `multiple testing` | p. 34 (deux), p. 35 (une) ; `multiple hypothesis` p. 4 ; `false discover` p. 4 et p. 34 |
| `Bonferroni`, `Holm` | aucune occurrence |
| `pre-regist` | aucune occurrence |
| `pre-commit` | p. 12, une occurrence (protocole engagé d'avance) |
| `hash`, `seal` | aucune occurrence |
| termes ajoutés : `deflated` | p. 35 seulement (heuristique fonctionnelle, aucun calcul) ; `scaled intercept` p. 34 seulement ; `redundan` p. 13, 17, 35 ; `memory` p. 2, 4, 12, 17, 35, 37 ; `code` p. 1, 9, 10, 12, 52 (aucune annonce de code publié) ; `github` p. 1 et p. 47 (la page du projet) ; `open source` : aucune occurrence |
| nom du modèle de langue utilisé | non trouvé : les noms de modèles (p. 8, 9, 48, 50) sont ceux de travaux cités ; ni nom, ni consigne, ni température du modèle du système dans les 60 pages |

## 3. Lecture du PDF par composante

### P — juger contre le connu, non contre aucun effet

- **La règle de promotion écrite teste contre aucun effet.** Algorithme 1, p. 13 : « if tIC ≥ τsig and SRLS ≥ τecon then » ; éq. 3.10, p. 16 : « Promote if tIC ≥ τsig and SRLS ≥ τecon », avec « where τsig , τecon , and τf ail denote the thresholds for statistical significance, economic viability, and outright failure, respectively. » La statistique t_IC est celle du coefficient d'information moyen contre zéro (éq. 3.7, p. 15 : « The system then aggregates these into a t-statistic »).
- **Le principe est affirmé en deux endroits, sans formule.** P. 34 : « Furthermore, we evaluate the factor’s contribution to reducing pricing errors, a concept aligned with the Scaled Intercept (SI) metric in Harvey and Liu (2021), ensuring that new factors provide incremental explanatory power relative to established benchmarks. » P. 35 : « Our agent emulates this skepticism by incorporating a multi-objective promotion gate » ; premier critère : « Using a memory-update mechanism, the agent ensures that new factors provide significant marginal information over existing benchmarks (e.g., the Fama-French five-factor model Fama and French (2015)). » ; « By filtering for marginal information gain, the framework avoids the “substitution effect” ».
- **À qui le texte attribue ce filtre.** Il l'attribue au mécanisme de mise à jour de la mémoire, cinquième module (p. 12 : « The fifth module is memory and policy update. It reads structured logs from prior rounds and generates the next candidate set »), que l'article place dans le modèle de langue : algorithme 1, ligne 30, p. 13, « Sk ← LLM(Sk−1 , Ek , Lk ) », annoté « Update search policy via reflection » ; éq. 3.11, p. 16, « where St is the current knowledge state, Et represents the empirical feedback from the evaluator, and Lt is the structured log of failed and successful hypotheses. » ; p. 17, « The next policy update uses this state to avoid redundant trials » ; p. 37, « By utilizing a memory-update mechanism, the agent refines its search strategy based on accumulated backtesting evidence ». Même chose pour le second critère de la p. 35 (« Factors are penalized for excessive turnover and rapid alpha decay. »), que la p. 38 rend à l'apprentissage de l'agent : « where it learns to penalize high-turnover signals that offer thin alpha cushions ». Dans l'algorithme, l'étiquette de redondance tient au seul seuil d'échec sur t_IC : « else if tIC < τf ail then », puis « D(f ) ← Redundant/Discard » (p. 13).
- **Le connu n'est mesuré qu'après la sélection, hors échantillon.** L'introduction l'annonce ainsi (p. 4) : « This confirms that the agent does not merely repackage known risk premia » ; la p. 26 conclut que « the best agent-generated signals are not merely repackaging canonical equity factors. » Exhibit 8, p. 25 : « This table presents annualized out-of-sample alphas and corresponding t-statistics » ; « Alphas are estimated via time-series regressions of long-short portfolio returns on the CAPM » (puis FF3, FF5, FF6). Annexe B.3, p. 55 : « We further evaluate this spread using risk-adjusted alphas to ensure that the agent’s discovered signals extract information that is not spanned by existing common risk factors. » ; conclusion, p. 45 : « deliver statistically significant risk-adjusted returns that are not spanned by standard asset pricing models ». Lecture de la table (p. 25), sans en tirer de conclusion sur la porte, qui est calculée sur l'échantillon de sélection : sept des douze facteurs (2, 4, 5, 7, 10, 11, 12) ont, hors échantillon, une statistique de Student de l'alpha FF5 inférieure à 3,0 en valeur absolue ; tous les douze sont les constituants de la combinaison (p. 39 : « This table lists the constituent factors used in the composite factor construction ») ; l'article le dit lui-même (p. 23) : « it does not imply that every promoted factor is equally investable on a standalone basis. »
- **Comparaison à un cadre de référence.** P. 43 : « we compare factors generated by the agentic framework against those from traditional AI factor mining » ; c'est une comparaison de portefeuilles a posteriori, non un nul de promotion.
- **Aucune valeur ni table de l'apport marginal** : aucune table ne donne, pour les facteurs promus, une mesure d'ordonnée à l'origine réduite, un test d'apport sur FF5 ou les valeurs de la porte sur l'échantillon de sélection (2004-2020) ; les tables dont la légende dit la période sont hors échantillon (p. 22, 25, 27, 31, 43).
- **Statut : voisin.** Principe affirmé (p. 34, 35), attribué par le texte à la mémoire de l'agent, calcul non montré ; le connu (modèles de facteurs fixés) n'est mesuré qu'a posteriori.

### (i) — proposeurs modèles de langue

- P. 13, ligne 6 : « Agent generates candidate factors Fk = {f1 , . . . , fn } via G based on state Sk−1 » ; p. 12 : « This strict separation between language-based proposal and code-based computation prevents hidden numerical drift » ; p. 11 : « the agent is free to propose new ideas only within explicit scientific constraints » ; p. 33 : « The mathematical expression of a factor and its economic rationale are produced jointly rather than sequentially. » ; p. 52 : « the agent is required to verbalize an economic rationale rt before producing the mathematical expression at ».
- Le modèle de langue utilisé n'est pas nommé dans les 60 pages (section 2) ; p. 53 : « It is important to emphasize that Eq. A.1 through Eq. A.4 serve as a conceptual framework to formalize the generative process of the Large Language Model (LLM), rather than an analytically tractable econometric model. »
- **Statut : pris.**

### (ii) — nul formé d'une mise en commun ajustée des lois prédictives de l'archive

- Les seules lois connues nommées sont des modèles de facteurs fixés (CAPM, FF3, FF5, FF6 ; p. 25, 28, 35), utilisés en régression a posteriori. La bibliothèque des facteurs promus (algorithme 1, p. 13) n'est jamais un terme de comparaison écrit : aucune règle ne compare un candidat aux facteurs déjà admis, hors la mention de la mémoire qui évite les essais redondants (p. 17). Aucune mise en commun de lois prédictives, aucun nul ajusté de l'archive dans les 60 pages.
- **Statut : voisin (lointain).** Je garde voisin, comme la v2, dans le sens non flatteur : un modèle de facteurs fixé, affirmé comme référence de l'apport marginal (p. 35), sans formule. Le constat non trouvé vaut pour la mise en commun ajustée de l'archive elle-même.

### (iii) — e-processus (ou validité à tout instant d'arrêt) comme règle de promotion

- Aucune occurrence des termes de la section 2 (e-valeur, e-processus, martingale, arrêt optionnel, test séquentiel, rapport de vraisemblances, facteur de Bayes).
- Règle de promotion à seuils fixes : p. 16 « A candidate is promoted only if it satisfies minimum statistical thresholds under the fixed protocol. » Seuil de signification relevé pour la multiplicité : p. 34 « To account for the thousands of implicit regressions performed during the discovery process, we eschew the traditional t > 2.0 threshold. », éq. 6.1 « |t-statistic| > 3.0 », « By requiring a t-stat of 3.0 ». Le texte ne relie pas le 3,0 au symbole τsig ; les valeurs de τecon et de τfail ne sont données nulle part dans les 60 pages.
- **Statut : voisin** (règle de promotion à seuil sur une statistique de Student à taille fixée) ; e-processus et validité à tout instant d'arrêt : **non trouvés**.

### (iv-a) — prédictions engagées (scellées) avant que les données existent

- P. 12 : « Our evaluation protocol is pre-committed before iterative search begins. » ; p. 16 : « is determined by a set of pre-defined thresholds » ; p. 12 : « Because the same protocol is reused across rounds, gains in performance can robustly attributed to the superiority of the generated hypotheses » (faute de l'original recopiée).
- Les données existent toutes avant la recherche : p. 17 « covering January 2004 through December 2024 » ; p. 18 « The iterative promotion gate is determined using data through December 2020 » ; p. 35 « All factor discovery and agent learning are finalized using data prior to December 2020. » ; la mise à l'écart de la période 2021-2024 est une séparation par conception, dite et non scellée : p. 14 « promotion gates are computed exclusively on the in-sample segment, and out-of-sample outcomes are never used to revise thresholds, re-rank candidates, or update the next-round search policy. » ; p. 36 « This blind test ensures that the performance reported is not a result of look-ahead bias or iterative over-fitting to recent market regimes. »
- Même règle p. 20 : « the selection stage is always computed on the in-sample segment only. »
- Traces : p. 16 « At the end of each round, the system writes a structured experiment record containing candidate definitions, metric outputs, gate outcomes, and next-step actions. » ; p. 21 « Each round records candidate definitions, evaluation statistics, and selection outcomes, allowing the full research path to be reconstructed ex post. » Ni empreinte, ni scellement, ni horodatage, ni dépôt des seuils (`hash`, `seal`, `pre-regist` : zéro occurrence). Ces journaux ne sont pas publiés dans le dépôt de la page du projet (section 4). Rien n'exclut, dans les 60 pages, que les données 2021-2024 aient été vues par le modèle de langue lors de son entraînement ; l'article ne l'aborde pas (`cutoff`, `pretrain` : zéro ; `pre-trained` p. 34 et 53 au sens des connaissances du modèle).
- **Statut : voisin** (protocole dit engagé d'avance, non scellé ; valeurs de deux seuils sur trois absentes ; données déjà existantes).

### (iv-b) — statistique calculée hors des agents

- P. 10 : « In each round, the system generates hypotheses, computes factor values, evaluates candidates under a fixed protocol, applies promotion gates, and updates the next search policy using accumulated evidence. » P. 12 : « The third module is a unified evaluator, which computes a common metric set for every candidate; no factor receives customized scoring logic. » ; « The fourth module is a transparent gatekeeper that converts evaluation outputs into explicit decisions: promote, hold for review, or retire. » ; p. 14 : « The promotion decision D is a mapping that depends only on the IS history » ; p. 13 : « evaluation thresholds Θ = {τsig , τecon , τf ail } ».
- Borne : la partie de la porte qui toucherait au connu (apport marginal, pénalité de rotation) est rendue à la mémoire de l'agent (p. 35, 37, 38) ; seule la porte sur t_IC et Sharpe est écrite comme calculée hors de l'agent. Ce que l'agent reçoit : p. 53 « the agent receives an observation ot from the environment E (e.g., Sharpe ratio, information coefficient, or execution errors) ».
- **Statut : pris** pour la porte sur t_IC et Sharpe (contre aucun effet) ; non établi pour l'apport marginal.

### Multiplicité

- Annoncée dès le résumé (p. 1 : « To mitigate data snooping biases, this closed-loop system imposes strict empirical discipline through out-of-sample validation and economic rationale requirements. ») et p. 4 : « By applying multiple hypothesis testing adjustments and evaluating out-of-sample signal decay, we demonstrate that the Agentic AI systematically resists p-hacking. » Réalisée, dans les 60 pages, par le seul seuil |t| > 3,0 (p. 34) ; la p. 35 dit : « Our multi-objective gate acts as a functional heuristic for the Deflated Sharpe Ratio, implicitly accounting for the hidden trials involved in automated factor search by imposing stringent non-performance hurdles. » Aucun ratio de Sharpe dégonflé calculé, aucune procédure de Bonferroni, de Holm ou de taux de fausses découvertes. Le nombre de tours K et le nombre de candidats essayés ne sont pas donnés (seulement les milliers de régressions implicites, p. 34). Argument d'a priori, sans calcul : p. 34 « the requirement of an explicit economic rationale acts as a Bayesian prior that drastically shrinks the hypothesis search space », « This fundamentally reduces the multiple-testing burden before any statistical hurdles are even applied. »

## 4. Lecture du code

Fichiers (`git ls-files`, commit `cc8bd7d06c26f39dc379157208482fe0da19623e`) : `README.md`, `chart_data.json`, `index.html`, `project-framework.png`. Aucun fichier de licence.

- **Aucun code du système.** Pas de générateur par modèle de langue, pas d'évaluateur, pas de porte, pas de mémoire, pas de journal de tours, pas d'empreinte. `README.md`, ligne 1, est tout le fichier : « # agentic-factor-investing ». Le seul programme est le JavaScript d'affichage de la page : `index.html`, l. 479, « fetch('chart_data.json').then(function(r) { return r.json(); }).then(initChart); ».
- **Données du graphique** : `chart_data.json`, ligne 1, liste de 502 points (date, linéaire, arbre) de 2021-01-04 à 2024-12-27 : premier point « [{"d":"2021-01-04","l":0.0152,"g":0.0146} », dernier « {"d":"2024-12-27","l":5.2805,"g":6.036}] » ; légende, `index.html` l. 356 : « Long-short cumulative return, out-of-sample. Hover for values; click legend to toggle series. »
- **Ce que la page dit de la porte et du connu** (texte, aucune réalisation) : l. 320 « AI agents propose and combine candidate signals; a disciplined gate keeps only what works. » et « What you see here is judged strictly on out-of-sample performance—no overfitting, no backtest bias. » ; l. 392 « One gate for all candidates. Factors that pass enter the library; we then build composite scores with linear and tree models. » ; l. 397 « We judge on data never used for selection. Performance shown gross and net of costs; edge tested against standard factor controls. » ; l. 375 « The edge stays significant after market, size, value, profitability, investment, and momentum. Not explained away by standard factors. » La comparaison au connu y est, comme dans le PDF, une mesure a posteriori contre des modèles de facteurs.
- **Référence de comparaison de la page** : l. 362-364 « <span class="tag">Baseline</span> <h3>Agentic vs off-the-shelf LLM</h3> <p class="muted">The agentic pipeline delivers stronger ranking power and better compounding than zero-shot LLM factors; the process design drives the edge.</p> » ; l. 488 « Agent-driven discovery and combination beat naive LLM baselines. Gate, library, and combination design make the difference. » Le PDF nomme autrement sa référence (cadre classique d'extraction de facteurs, p. 43).
- **Écart entre la page et le PDF** (constat, sans interprétation) : l. 368-370 « <div class="metric metric-sharpe">Sharpe</div> <div class="metric-value">Linear 3.82 &nbsp;/&nbsp; Tree 6.02</div> <p class="muted">Long-short gross, out-of-sample.</p> », alors que le PDF donne 2,75 pour la combinaison linéaire hors échantillon (exhibit 9, p. 27 ; résumé p. 1) ; le dernier point linéaire du graphique (5,2805) ne coïncide pas avec le rendement de période de l'exhibit 9 (470,43 %, p. 27). Le commit date du 14 mars 2026 (`git log`), la v2 du PDF du 6 avril 2026 (p. 1, en-tête arXiv).
- **Code publié ailleurs ?** Le PDF n'annonce aucun code : p. 47 « Data will be made available on request. Additional interactive results, methodological documentation, and replication details are available at the project homepage » ; p. 1 « Project homepage: https://allenh16.github.io/agentic-factor-investing/ ». La page renvoie, pour la méthode et la réplication, à un fichier qui ne contient que son titre : l. 503 « For methodology and replication, see the project <a href="README.md">documentation</a>. » Aucun autre dépôt n'est cité dans les 60 pages ni dans les trois fichiers.

## 5. Réponses aux questions propres à la pièce

1. **Nœud 1 de la v2 — l'apport marginal sur le modèle à cinq facteurs est-il une règle de promotion calculée hors de l'agent ?** Non trouvé comme tel dans les 60 pages ni dans le dépôt. Il est **affirmé** (p. 34, 35), sans formule, sans statistique, sans seuil, sans résultat ; la seule règle formelle de promotion (algorithme 1, p. 13 ; éq. 3.10, p. 16) porte sur t_IC et Sharpe contre aucun effet ; et, là où le texte dit qui fait le filtre, il le rend au mécanisme de mise à jour de la mémoire, c'est-à-dire au modèle de langue (p. 13 ligne 30, p. 16, p. 35, p. 37). Borne (R8) : le code du système n'est pas publié ; on ne peut pas exclure qu'un tel filtre existe dans un code non publié. Dans le sens non flatteur, je ne l'exclus pas ; je dis seulement qu'il n'est montré nulle part.
2. **Le protocole dit *pre-committed* (p. 12) est-il scellé ?** Décrit seulement : aucune empreinte, aucun scellement, aucun horodatage, aucun dépôt public du protocole ni des seuils ; deux des trois seuils (τecon, τfail) n'ont pas de valeur écrite ; les journaux de tours (p. 16, 21) ne sont pas publiés dans le dépôt de la page.
3. **Multiplicité, e-valeur, validité à tout instant d'arrêt ?** Multiplicité : un seuil fixe relevé à |t| > 3,0 (p. 34) et une heuristique dite fonctionnelle du Sharpe dégonflé, non calculée (p. 35) ; aucune procédure de contrôle (Bonferroni, Holm, taux de fausses découvertes : zéro occurrence) ; nombre d'essais non donné. E-valeur, e-processus, validité à tout instant d'arrêt : zéro occurrence.

## 6. Table pris, voisin, non trouvé (BEYOND seule)

| composante | statut | preuve |
|---|---|---|
| P | **voisin** | apport marginal sur FF5 affirmé (p. 34, 35), attribué à la mémoire de l'agent (p. 13 l. 30, p. 16, 37), sans formule ni résultat ; porte écrite contre aucun effet (p. 13, 16) ; alphas contre CAPM à FF6 a posteriori, hors échantillon (p. 25, 55) |
| (i) | **pris** | p. 13 l. 6 ; p. 12 (proposition par le langage, calcul par le code) ; modèle non nommé |
| (ii) | **voisin (lointain)** | modèles de facteurs fixés comme référence, a posteriori (p. 25, 28) ou affirmée (p. 35) ; aucune mise en commun ajustée de lois de l'archive ; bibliothèque des admis jamais nul écrit |
| (iii) | **voisin** pour la règle à seuil ; **non trouvé** pour l'e-processus | p. 16 et 34 (valeur absolue de t > 3,0, taille fixée) ; zéro occurrence des termes séquentiels (section 2) |
| (iv-a) | **voisin** | p. 12 et 16 (engagé d'avance, seuils prédéfinis), non scellé ; données 2004-2024 déjà existantes (p. 17, 18, 35) |
| (iv-b) | **pris** (porte t_IC et Sharpe) | p. 12, 13, 14 ; non établi pour l'apport marginal (p. 35, 37, 38) |
| conjonction | **non trouvée dans BEYOND** | manquent (ii), (iii) sous forme d'e-processus, le scellement de (iv-a), des prédictions faites avant que les données existent |
| code | **absent** | dépôt de la page : `README.md` l. 1, `index.html` l. 479 et 503 ; aucun code du système |

## 7. Changements par rapport à la v2 (`lecture-pdf-priorite-haute-o4-v2.md`, section 3.1, 4, 6)

| constat | v2 | cette lecture | change ? |
|---|---|---|---|
| Profondeur | lu en entier p. 12, 34, 35 ; lignes filtrées p. 14, 16, 55 ; p. 1-47 en texte déclaré en v1, non regaranti | 60 pages sur 60, annexes comprises ; figures non lues comme images | **oui** (profondeur) |
| Code | non lu | dépôt de la page lu : aucun code du système ; aucun autre code annoncé | **oui** (code non lu devient : code du système non publié dans le dépôt annoncé) |
| Apport marginal | affirmé comme partie de la porte, calcul non montré ; filtre peut-être dans le code | même chose, plus : attribué par le texte au mécanisme de mémoire, que l'algorithme place dans le modèle de langue (p. 13 l. 30, p. 16, 35, 37) ; la pénalité de rotation aussi (p. 38) ; aucune valeur ni table ; l'étiquette de redondance de l'algorithme tient au seul seuil d'échec sur t_IC (p. 13) | **précision** (statut inchangé, nœud 1 reformulé) |
| Engagement p. 12 | affirmé, non scellé ; données existantes | confirmé ; en plus : τecon et τfail sans valeur dans les 60 pages ; journaux de tours non publiés | **précision** |
| Seuil de 3,0 sur la valeur absolue de t | trouvé ; lien à τsig non écrit | confirmé sur le texte entier | non |
| Multiplicité | heuristique du Sharpe dégonflé (p. 35) | confirmé ; en plus : l'annonce de la p. 4 n'est réalisée que par le seuil 3,0 ; nombre d'essais non donné ; aucune procédure | **précision** |
| Termes séquentiels | aucune occurrence (7 termes) | aucune occurrence ; liste étendue aux 23 termes de la consigne, plus des termes ajoutés (section 2) | non (portée élargie) |
| Statuts P, (i), (ii), (iii), (iv-a), (iv-b) | voisin, pris, voisin, voisin, voisin, pris | identiques ; (iii) précisé : voisin pour la règle à seuil, non trouvé pour l'e-processus ; (iv-b) borné à la porte t_IC et Sharpe | **non** pour les statuts |
| Page du projet | non lue | écart avec le PDF (Sharpe 3,82 et 6,02 contre 2,75), référence dite LLM sans entraînement spécifique | **nouveau** constat, hors O4 |
| Verdict O4 | occupée en partie | non modifié par cette lecture | non |

## 8. Nœuds pour Lazar (décisions à prendre, pas des conclusions)

1. **Formulation de BEYOND dans la note d'englobement (prochaine version).** Proposition, en italique : *voisine ; règle de promotion calculée hors de l'agent, contre aucun effet (t_IC et Sharpe à seuils, valeur absolue de t supérieure à 3,0) ; apport marginal sur le modèle à cinq facteurs affirmé et attribué à la mémoire de l'agent, sans formule ni résultat dans les 60 pages ; protocole dit engagé d'avance, non scellé ; code du système non publié*. Options : (a) l'adopter (avantage : exacte sur pièce entière ; inconvénient : aucun) ; (b) garder la ligne v2 (avantage : rien à changer ; inconvénient : laisse ouvert un code qui n'est pas publié). Recommandation : (a), confiance moyenne à haute. Le statut ne bouge pas.
2. **Demander le code ou les journaux aux auteurs ?** Le PDF promet les données sur demande (p. 47) ; la page renvoie à un fichier vide. Options : (a) rédiger une demande (contact extérieur : je rédige, tu envoies) ; (b) laisser la pièce bornée à ce qui est publié. Recommandation : (b) pour O4, la pièce étant voisine par des composantes déjà occupées ailleurs (SEADS) ; confiance moyenne.
3. **Réserve de fiabilité sur la pièce.** Les chiffres de la page du projet ne sont pas ceux du PDF (section 4). Options : (a) noter une réserve si BEYOND est citée dans un texte public ; (b) ne rien noter (hors O4). Recommandation : (a), confiance moyenne.
4. **Citation obligatoire ?** BEYOND décrit un protocole engagé d'avance et une porte hors du modèle pour des facteurs proposés par un modèle de langue. Décision : l'ajouter ou non à la liste des citations obligatoires de O4 (N-067), à côté de SEADS, comme voisin de (i), (iv-a) affirmé et (iv-b).

## 9. Ce qui reste non lu

- Contenu graphique des figures du PDF et `project-framework.png`.
- Historique du dépôt avant le commit `cc8bd7d` (clone superficiel ; le message du commit parle d'un fichier renommé, `git log`) ; page du projet en ligne (aucun accès réseau ; seul le clone est lu).
- Version v1 de arXiv 2603.14288.
- Références citées : Harvey et Liu 2021 (mesure d'ordonnée à l'origine réduite), López de Prado 2018 (Sharpe dégonflé), Harvey, Liu, Zhu 2016.
- Tout code éventuel non publié (borne de R8).

## 10. Incidents et refus

- Aucun refus de permission, de crochet ou de classifieur rencontré.
- Aucun accès réseau, aucune dépense, aucun programme du clone lancé (le JSON est lu par `python3 -I` et le module standard, comme donnée).
- Écart mineur à la consigne, déclaré : un `ls` du dossier nommé `docs/notes/lecture-o4-suite-v1/` (pour situer les programmes de rejeu) et du dossier `docs/sources/code/lecture-o4-v1/` (pour placer la provenance) ; aucun fichier de ces listes lu hors des fichiers nommés.
- Contrôle strict des citations : 59 sur 61, écart dû aux césures de fin de ligne (en-tête).
