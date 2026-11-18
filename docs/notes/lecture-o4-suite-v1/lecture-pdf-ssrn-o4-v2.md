# Lecture sur PDF de SSRN 6569258 (version officielle de septembre 2026) et de SSRN 6474601 contre O4 — v2

- **Auteur** : modèle A (session du compte organisme), tâche 3 du brief ; v1 écrite à 2026-11-14T22:55:43Z (`date -u`). Lectures faites par deux **Version 2** écrite à 2026-11-14T23:10:09Z (`date -u`) : R12, la v1 (`5b98cc32ed59c7ce6f7efde073c81dad28d04bdd19cfafe00478242e3376b8f8`) reste en place ; porte la contre-lecture du modèle H (`contre-lecture-lecture-pdf-ssrn-o4-v1.md`, `f8d415a7…`, « tient avec réserves », 0 bloquant, 1 majeur, 6 mineurs ; section 7).
  sous-agents du même modèle A (un par PDF), chacune soumise à un **vérificateur adverse d'un autre modèle** (modèle E : même modèle
  que les lecteurs E, F, G des vérifications courtes du pilote, instances neuves), qui a rejoué chaque citation par programme et
  cherché à réfuter chaque statut. Quatre agents au plus ; aucun n'a écrit de fichier ; **aucun refus** d'outil, de crochet ni de
  classifieur ; aucune dépense, aucun accès réseau.
- **Règles (R7, R8)** : « non trouvé » = non trouvé dans les pages lues, avec leur profondeur (section 5) ; rien n'est déclaré libre ;
  pages = pages du PDF. Tout écart au verdict de la note d'englobement (`docs/notes/lecture-o4-englobement-v1.md`, `f521e164…`) est un
  **nœud pour Lazar**, jamais une conclusion.
- **Citations** : 91 passages (57 des lecteurs, 6 ajoutés par les vérificateurs, 12 d'avril et 11 de septembre pour la correspondance,
  5 ajoutés après la contre-lecture et vérifiés par l'auteur : A13, A14, K31 à K33), rejoués par `rejouer_citations_ssrn_o4_v1.py` sur
  `citations-ssrn-o4-v4.json` : **91 sur 91** (`rejeu-citations-ssrn-o4-v4.json`).
  Les versions 1 et 2 du fichier de citations sont gardées : la v1 portait, dans sept textes de septembre, des remarques du lecteur
  entre parenthèses (79 sur 86) ; la v2 les a portées en note, et gardait une virgule doublée (85 sur 86) ; la v3 la retire. Aucun mot
  cité n'a été changé. La v4 ajoute les cinq passages de la contre-lecture ; la v3 reste en place.

## Pièces lues

| pièce | chemin (sur `main`) | sha256 (égal au compagnon) |
|---|---|---|
| **LIU, version officielle** : Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, « September, 2026 », 84 p., déposée par Lazar | `docs/sources/pdf/ssrn-lazar-2026-11-14/liu-liu-liu-mei-2026-can-ai-do-financial-research-ssrn-6569258.pdf` | `15cdb423744d78855ce3e5c3096e404961a4676634cb5fe88b0abaaa65c1bfcf` |
| **LIU, copie d'avril** (hôte d'une conférence ; lue par la note d'englobement) : 71 p. ; différente octet pour octet de la version officielle | `docs/sources/pdf/lecture-o4-v1/ssrn-6569258/liu-liu-liu-mei-2026-can-ai-do-financial-research-skbi-smu-copie-v1.pdf` | `2d4e1d61d248699aaaf73b20dbb83ed41d928888814436dca633ffffa9cd83f5` |
| **KL** : Koijen, Levy, « Assessing the Benefits of Optimized Agentic AI Systems for Asset Pricing », SSRN 6474601, « June 30, 2026 », 39 p., déposée par Lazar | `docs/sources/pdf/ssrn-lazar-2026-11-14/koijen-levy-2026-optimized-agentic-ai-asset-pricing-ssrn-6474601.pdf` | `98757745f4364034afa71ba70e78c56103f90822ab4a744ff77e90cd6cee5a2e` |
| provenance des deux PDF déposés | `docs/sources/pdf/ssrn-lazar-2026-11-14/provenance-v1.md` | `3b62cec5e0059fbc…` |

O4 lue : « juge statistique dont le nul est formé des lois déjà connues (l'archive) : une fiche n'est promue que si sa prédiction
scellée bat ce que l'archive prédit déjà » (N-067, section 4) ; composantes de la note d'englobement (section 0, point 5) : **P** le
principe « une découverte se juge contre ce qui est déjà connu, non contre aucun effet » ; **(i)** proposeurs modèles de langue ;
**(ii)** nul formé d'une mise en commun ajustée des lois prédictives de l'archive (lois connues et survivantes promues par le système) ;
**(iii)** e-processus comme règle de promotion ; **(iv)** prédictions scellées avant que les données existent, statistique hors des
agents.

## 0. Verdict

**O4 reste « occupée en partie ».** Les deux PDF lus ajoutent à la partie occupée ; aucun ne porte la conjonction (i)+(ii)+(iii)+(iv).

1. **LIU, version officielle de septembre** : P **trouvé**, plus nettement qu'en avril (« subsumed by what is already known », p. 6 ;
   porte de survie contre les prédicteurs publiés, p. 30, qui fait passer les candidats de 103 à 11, p. 32) ; (i) trouvée ; (ii) en
   partie (nul des lois connues par régression contre dix prédicteurs publiés et trois modèles de facteurs, **après** la course et hors
   de la boucle, p. 11, 22) ; (iii) non trouvée (aucune e-valeur sur les 84 pages) ; (iv) en partie (sens déclaré avant le résultat,
   statistique hors des agents ; données de 1963 à 2024 antérieures à l'engagement ; le test prospectif gelé est dit **non fait**,
   p. 6, 34). **Une phrase de la note d'englobement ne tient plus sur cette version** : « it lacks direct access to factor model results
   during the discovery loop » (avril, p. 36) est **absente**. Elle était déjà en tension avec la copie d'avril elle-même : en avril,
   le retour fait au proposeur portait déjà la statistique de l'alpha (A13, p. 15), alpha des quatre facteurs de Carhart (A14, p. 14) ;
   en septembre, il porte un alpha à cinq facteurs (p. 19, 57) : **seul le modèle de facteurs change** (correction de la v1, constat M1
   de la contre-lecture). L'argument devient : aucune règle de promotion ni aucun nul formé de l'archive dans la boucle ; le retour
   contient, en avril comme en septembre, un alpha contre un modèle de facteurs fixé.
2. **KL, Koijen et Levy (30 juin 2026), pièce neuve pour O4** : P **trouvé** pour des systèmes à modèle de langue optimisés, jugés par
   leur gain d'explication sur des déterminants connus (p. 1, 8, 13) ; (i) trouvée (optimiseurs à modèle de langue, p. 17, 18) ;
   (ii) en partie (régression ajustée sur des contrôles connus, dans l'évaluation et dans la boucle, p. 16 ; le système optimisé est
   aussi jugé contre le système non optimisé avec la surprise, K32, K33, ce qui est une forme de « meilleur système en place » ; un
   livre de règles qui grandit existe, K31, mais il est versé dans le prédicteur, non dans le nul ; aucune mise en commun ajustée des
   lois d'une archive comme nul) ; (iii) non trouvée ; (iv) **en partie, et plus près d'O4 que LIU et SEADS** : banc d'essai en temps
   réel, prédictions recueillies avant que le rendement de l'annonce n'existe, avec la seule information disponible à l'annonce (p. 1,
   3, 11) ; ni scellement ni horodatage trouvé ; pour les systèmes optimisés, le texte ne dit pas que les prédictions de la seconde
   moitié du trimestre ont été émises avant les événements (p. 16), même si le protocole temporel est dit strict observation par
   observation (KO1, KO2, p. 11). Deux réserves sur P pour KL : ce qu'on juge est un prédicteur, pas une découverte isolée ; et la
   comparaison des règles apprises aux modèles existants est une perspective, pas un test (p. 4, 23).
3. **Condition de N-067** (« libre hors du dépôt seulement après lecture sur PDF de SSRN 6569258 et des pistes de priorité haute ») :
   la lecture sur PDF de SSRN 6569258 est **faite, sur la version officielle, à la profondeur dite à la section 5** (aucun PDF lu en
   entier ; pages lues en entier et pages lues par recherche de termes distinguées ; les pistes de priorité haute ne sont lues que par
   sections, lecture v2) ; SSRN 6474601 est lu à la même règle. Le résultat ne permet **pas** de
   déclarer O4 libre : il confirme et étend l'occupation du principe. Reste non lu, de la liste de priorité haute : la version de la
   revue de Novy-Marx et Velikov (JEL 64(1)) et le code d'EvoSCM, de BEYOND et de WAHL (lecture v2, section 7).

**Nœuds de revendication pour Lazar** (décisions, non conclusions) :
- **N-SSRN-1** : remplacer, dans la note d'englobement et dans toute phrase publique, les pages et textes d'avril de LIU par ceux de la
  version officielle (section 1) ; retirer l'appui sur la phrase d'avril p. 36 (absente) ; dire le retour d'un alpha à cinq facteurs
  dans la boucle, comme il le faisait déjà en avril (alpha de Carhart, A13, A14).
- **N-SSRN-2** : porter KL comme pièce de la partie occupée, pour P et pour la partie « en temps réel » de (iv) : toute phrase publique
  qui revendiquerait « des prédictions faites avant que les données existent, jugées contre ce qui est connu, pour des systèmes à
  modèle de langue » doit citer Koijen et Levy (SSRN 6474601, p. 1, 3, 8, 11, 16). Antériorité : 30 juin 2026 est la date **imprimée** sur le PDF (et sa date de création), non la date de dépôt sur SSRN, qui n'est pas
  lue ; elle précède celle de SEADS (arXiv 2609.00731, 1er septembre 2026, selon la note d'englobement). La comparaison est faite avec
  SEADS, non avec ce programme.

## 1. LIU : correspondance des citations d'avril sur la version officielle

| id avril | page avril | citation d'avril (note d'englobement, section 3.1) | page septembre | état | id septembre |
|---|---|---|---|---|---|
| A01 | 1 | « novelty tests against 209 published anomalies » | 1 | modifiée | S01 |
| A02 | 1 | « 38 survive multivariate horse races designed to isolate signals with independent predictive content » | 1 | modifiée | S02 |
| A03 | 28 | « For each survivor, we compute its average cross-sectional Spearman rank correlation with each published anomaly, select the 10 closest neighbors, and estimate a multivariate Fama–MacBeth regression that includes the new signal together with those controls. » | 22 | modifiée | S03 |
| A04 | 28 | « Of the 34 survivors with stable conditional estimates, 9 retain significance at » | 32 | modifiée | S04 |
| A05 | 26 | « many are absorbed by known factor structures or closely related published signals » | 32 | modifiée | S05 |
| A06 | 18 | « our goal is to isolate signals with incremental predictive content rather than count every successful variant as a separate discovery » | 22 | modifiée | S06 |
| A07 | 4 | « To our knowledge, this is the first study to combine LLM-guided signal discovery with the full battery of modern multiple testing corrections, multi-model factor spanning, cross-anomaly novelty tests » | 5 | modifiée | S07 |
| A08 | 14 | « For purposes of the discovery loop, a proposal is classified as successful if its Fama–MacBeth » | 19 | modifiée | S08 |
| A09 | 36 | « it lacks direct access to factor model results during the discovery loop » | — | absente | — |
| A10 | 22 | « We do not claim out-of-sample validation from the discovery loop itself. » | 6 | modifiée | S10 |
| A11 | 22 | « Importantly, the AI research agent has no direct access to the raw CRSP/Compustat panel and does not alter the empirical protocol. » | 42 | modifiée | S11 |
| A12 | 8 | « proposes a hypothesis before the empirical result is known for that proposal » | 40 | modifiée | S12 |

Textes de septembre (rejoués sur la version officielle) :

- **S01** [p. 1] « We then test their stability over time, robustness across factor models, and incremental information relative to 209 published anomalies, identifying a small and robust set that survives the full pipeline. »
- **S02** [p. 1] « We apply multiple-testing corrections and jointly compare related formulas, retaining 52–68 candidates per run with distinct predictive content. »
- **S03** [p. 22] « For each candidate reaching the published-predictor stage, the spanning procedure selects up to ten predictors with the largest absolute average cross-sectional rank correlations, subject to the joint-coverage, rank, and conditioning requirements in Appendix A.6. » — (Le détail de l'algorithme est en p. 66-67.)
- **S04** [p. 32] « Of the 103 records entering this stage, 101 yield estimable regressions, 11 retain a direction-consistent conditional statistic above 1.96, and two fail because no valid conditional regression can be estimated. »
- **S05** [p. 32] « Many records that survive multiplicity and factor adjustment therefore contain information already represented by their selected published comparators. » — (Voisin p. 16 : « absorbed by known factors ».)
- **S06** [p. 22] « This horse race identifies incremental conditional return association relative to other constructions generated for the same economic task; it does not replace run-level multiplicity adjustment or establish statistical independence or economic novelty. » — (La course se tient désormais à l'intérieur de chaque paire de thèmes, p. 16, 21-22, 65.)
- **S07** [p. 5] « To our knowledge, this is the first study to combine autonomous LLM-guided signal discovery with modern multiple-testing corrections, alternative factor models, subsample and decay analyses, and spanning tests against published anomalies, »
- **S08** [p. 19] « We classify an empirically evaluated hypothesis as a first-pass success when its Fama– MacBeth statistic is finite, exceeds 1.96 in absolute value, and the estimated slope has the direction declared before evaluation; equivalently, dj tFMB,j > 1.96. »
- **S10** [p. 6] « First, the search is adaptive and uses the same historical panel throughout, so our post-discovery tests provide search-adjusted inference rather than true out-of-sample validation. » — (Voisins : p. 29, 34, 43.)
- **S11** [p. 42] « The LLM does not read firm-level observations, assign historical scores, access the raw CRSP– Compustat panel, or alter the portfolio-construction procedure. » — (Voisins : p. 2, « the agents choose which economic ideas to pursue but cannot alter how those ideas are tested » ; p. 57.)
- **S12** [p. 40] « Each hypothesis states an economic mechanism, an executable accounting expression, and a return direction before its own result is observed. » — (Voisin p. 13 : direction « declared before hypothesis j is evaluated ».)

## 2. LIU, version officielle : lecture par composante

| composante | statut | justification |
|---|---|---|
| P | **trouvée** | Le principe y est, pour des hypothèses de modèle de langue : jugement sur l'« incremental information relative to 209 published anomalies » (p. 1), « subsumed by what is already known » (p. 6), porte de survie contre les dix prédicteurs publiés les plus proches (p. 22, 30), qui élimine de 103 à 11 (p. 32), et revendication de priorité des auteurs (p. 5). Ce juge s'applique après la boucle. |
| i | **trouvée** | Agents modèles de langue en proposeur et en critique (p. 1, 11, 20-21, 57-58). |
| ii | **trouvée en partie** | Le nul des lois connues existe sous forme de régression de Fama et MacBeth contre les dix prédicteurs publiés les plus corrélés, et contre trois modèles de facteurs. Une course oppose aussi les découvertes du système entre elles, à l'intérieur de chaque tâche, par régression jointe et élimination descendante. Tout cela se fait après la recherche et hors de la boucle (p. 11, 22, 65-67). L'archive interne grandit (p. 15), mais elle ne sert que de contexte. Dans la boucle on ne trouve que trois choses : le crible « aucun effet » à 1,96 (p. 19) ; un alpha à cinq facteurs fourni comme retour (p. 19, 57) [v2 : déjà présent en avril sous la forme d'un alpha à quatre facteurs, A13, A14 ; la v1 le disait à tort nouveau] ; et des contrôles de nouveauté, soit d'identité des formules (p. 57), soit par le critique modèle de langue (p. 15, 38). Aucune mise en commun ajustée des lois prédictives de l'archive n'a été trouvée dans les pages lues, et rien de ce qui est promu par le système ne devient un nul de l'étape suivante. |
| iii | **non trouvée dans les pages lues** | Aucune occurrence de e-value, e-process, anytime ni martingale sur les 84 pages. L'inférence passe par des statistiques de Student à taille fixée, la méthode de Benjamini et Yekutieli à q = 0,05, une probabilité a posteriori du nul et un double bootstrap (p. 29-30, 63-65). Dwork et al. 2015 est cité comme cadre du problème, sans être employé (p. 43). |
| iv | **trouvée en partie** | Le sens de chaque prédiction est déclaré avant son résultat (p. 13, 40), et la statistique est calculée hors des agents par du code déterministe (p. 11, 42). En revanche, les données de 1963 à 2024 existaient avant l'engagement (p. 17, courses d'août 2026 p. 58). Aucun scellement par empreinte ne porte sur les prédictions : le seul scellement est celui du livre de codage (p. 70, 72). Le test prospectif gelé est décrit comme non fait (p. 6, 34, 43). |

Citations (rejouées, 86 sur 86 pour l'ensemble) :

| id | page | composante | citation (texte de `pdftotext`, espaces réduits) | ce qu'elle établit |
|---|---|---|---|---|
| L01 | 1 | P | « incremental information relative to 209 published anomalies » | Le principe est toujours là dans le résumé : les hypothèses retenues sont jugées sur ce qu'elles apportent en plus de 209 anomalies publiées. |
| L02 | 6 | P | « where seemingly new evidence is subsumed by what is already known » | Nouveau dans cette version : les auteurs disent en toutes lettres qu'une découverte se juge contre ce qui est déjà connu. |
| L03 | 30 | P | « Finally, the record must retain its declared direction and a conditional statistic above 1.96 after controlling for up to ten selected nearby predictors from the Chen–Zimmermann library (Chen and Zimmermann, 2022). » | Le principe sert de porte de survie : une hypothèse n'est retenue que si son effet tient une fois contrôlé par les prédicteurs publiés qui lui ressemblent le plus. |
| L04 | 32 | P | « Many records that survive multiplicity and factor adjustment therefore contain information already represented by their selected published comparators. » | Le juge contre le connu élimine en pratique : il fait passer les candidats de 103 à 11. |
| L05 | 5 | P | « To our knowledge, this is the first study to combine autonomous LLM-guided signal discovery with modern multiple-testing corrections, alternative factor models, subsample and decay analyses, and spanning tests against published anomalies » | Les auteurs revendiquent toujours la priorité, avec une formulation nouvelle (tests d'englobement contre les anomalies publiées). |
| L06 | 1 | i | « We place specialized large language model agents in an environment with a symbolic language of interpretable accounting formulas and a fixed empirical evaluation pipeline. » | Les proposeurs sont des modèles de langue : la composante (i) est établie. |
| L07 | 11 | ii | « Once a run ends, post-search procedures operate outside the discovery loop and are indexed to the population for which each procedure is defined. » | Les tests contre les lois connues se font après la course et hors de la boucle de découverte ; ce ne sont pas des règles de promotion internes à la boucle. |
| L08 | 19 | ii | « We classify an empirically evaluated hypothesis as a first-pass success when its Fama– MacBeth statistic is finite, exceeds 1.96 in absolute value, and the estimated slope has the direction declared before evaluation » | Dans la boucle, le crible reste un nul « aucun effet » : un seuil de Student à 1,96 dans le sens annoncé. |
| L09 | 57 | ii | « Each archive entry reports the expression, declared direction, Fama–MacBeth statistic, long– short alpha and alpha statistic, Sharpe ratio, coverage, and any execution error. » | [v2 : le lecteur disait ce retour « nouveau » ; il ne l'est pas, A13 et A14 : seul le modèle de facteurs change.] Le retour fait au proposeur contient un alpha. Ce retour reste du contexte, pas une règle de promotion, et pas un nul formé de l'archive. |
| L10 | 19 | ii | « The discovery-stage alpha uses the Fama–French five-factor model » | Cet alpha de la boucle se calcule contre un seul modèle de facteurs fixé à l'avance, et non contre une mise en commun ajustée des lois de l'archive. |
| L11 | 15 | ii | « Within a given run, the archive is the state variable of the adaptive search. » | L'archive interne grandit à chaque génération (équation 3), mais elle sert de contexte au proposeur et au critique, pas de nul statistique. |
| L12 | 15 | ii | « whether the proposal materially differs from hypotheses already evaluated within the task » | Dans la boucle, la nouveauté par rapport à l'archive est jugée par le critique, qui est un modèle de langue, de façon qualitative et avant les résultats. Ce n'est pas un juge statistique. |
| L13 | 38 | ii | « The critic’s comparison set is limited to published signals invoked from its finance knowledge and proposals visible in the contemporaneous task archive; it is not an exhaustive literature review. » | Le critique compare chaque proposition au connu (signaux publiés tirés de sa mémoire, et archive) sans aucune statistique ; les auteurs le disent eux-mêmes. |
| L14 | 57 | ii | « Duplicate checks operate both within the current batch and against exact or normalized expressions in the prior task archive. » | Le seul contrôle déterministe contre l'archive fait dans la boucle est un contrôle d'identité des formules, pas de leur contenu prédictif. |
| L15 | 22 | ii | « This horse race identifies incremental conditional return association relative to other constructions generated for the same economic task » | Une course oppose les découvertes du système entre elles (archive interne), mais elle a lieu après la recherche, par régression jointe et élimination descendante, et non par une loi prédictive mise en commun. |
| L16 | 22 | ii | « For each candidate reaching the published-predictor stage, the spanning procedure selects up to ten predictors with the largest absolute average cross-sectional rank correlations » | Le nul des lois connues se réduit aux dix prédicteurs publiés les plus corrélés, mis en régression de Fama et MacBeth, et non à une mise en commun ajustée de toute l'archive. |
| L17 | 63 | iii | « Let pj denote the raw reference p-value supplied to the multiplicity procedures, » | L'inférence repose sur des valeurs p à taille fixée (loi normale, puis Benjamini et Yekutieli, Bonferroni, Holm) ; aucune e-valeur. |
| L18 | 29 | iii | « the run-level Benjamini–Yekutieli (BY) false-discovery-rate procedure at q = 0.05 » | La règle de promotion est une correction de multiplicité classique, pas un e-processus valide à tout instant d'arrêt. |
| L19 | 16 | iii | « should not be interpreted as end-to-end selective inference for the adaptive search algorithm. » | Les auteurs reconnaissent qu'aucune garantie ne couvre la recherche adaptative de bout en bout. |
| L20 | 43 | iii | « falls within the data-snooping and adaptive-data-analysis problems studied by White (2000); Harvey et al. (2016); Dwork et al. (2015); Russo and Zou (2016). » | Nouveau : l'analyse de données adaptative (Dwork et al. 2015, réserve réutilisable) est citée comme cadre du problème, mais l'outil n'est pas employé. |
| L21 | 40 | iv | « Each hypothesis states an economic mechanism, an executable accounting expression, and a return direction before its own result is observed. » | Chaque prédiction (son sens) est engagée avant le résultat de cette hypothèse, mais sur des données qui existent déjà. |
| L22 | 17 | iv | « The sample ends in December 2024. » | Avec les courses d'août 2026 (p. 58), cela établit que toutes les données existaient avant l'engagement : il n'y a aucune prédiction scellée avant que les données existent. |
| L23 | 6 | iv | « A true out-of-sample test would freeze the discovered hypotheses and all evaluation choices before new returns are realized, then evaluate them prospectively without further revision. » | Le test prospectif, gelé avant les données, est décrit, mais comme non fait : c'est une limite de l'article, pas une preuve que la case est vide dans le champ. |
| L24 | 34 | iv | « They remain candidates for prospective validation and external replication. » | Les survivants n'ont pas été validés sur des données postérieures. |
| L25 | 42 | iv | « The LLM does not read firm-level observations, assign historical scores, access the raw CRSP– Compustat panel, or alter the portfolio-construction procedure. » | La statistique se calcule hors des agents, par du code fixe : cette partie de (iv) est établie. |
| L26 | 11 | iv | « deterministic code enforces the admissible language, constructs the resulting signal, and applies the same empirical pipeline to every validated hypothesis. » | Le juge empirique est du code déterministe, séparé des agents. |
| L27 | 70 | iv | « Before coding, the codebook is frozen at SHA-256 » | Le seul scellement par empreinte de l'article porte sur le livre de codage de l'audit des mécanismes, pas sur les prédictions des hypothèses. |
| LO1 | 29 | (ajout du vérificateur) | « a record must clear seven cumulative gates: (1) the run-level Benjamini–Yekutieli (BY) false-discovery-rate procedure at q = 0.05; (2) the posterior-null-probability criterion; » | Règle de promotion à sept portes cumulatives, y compris des alphas contre trois modèles de facteurs et le test conditionnel contre les prédicteurs publiés. C'est la règle de promotion réelle, plus riche qu'un seul BY. Elle reste à taille fixée, après course, sans e-valeur, donc (iii) reste non trouvée. À citer à côté de la p. 29 déjà utilisée. |
| LO2 | 6 | (ajout du vérificateur) | « allowing future agents to learn from them rather than repeat them. » | L'archive cumulative est destinée à des agents futurs, ce qui rapproche de l'idée d'une archive qui devient connaissance disponible. Aucune règle statistique n'y est attachée dans le texte lu, mais la note devrait le mentionner pour ne pas laisser croire que l'idée d'archive réutilisée est absente. |
| LO3 | 62 | (ajout du vérificateur) | « no adjustment, bootstrap calibration, or selection threshold is estimated from a pooled cross-run population. » | Précise que rien n'est mis en commun entre courses : appuie le statut « trouvée en partie » de (ii), car l'archive d'une course ne forme pas le nul d'une autre. Utile comme pièce négative explicite. |

## 3. KL, Koijen et Levy : lecture par composante

| composante | statut | justification |
|---|---|---|
| P | **trouvée** | Les prédictions de systèmes à modèle de langue optimisés sont jugées par leur gain d'explication sur une base de déterminants connus (la surprise de bénéfice), recalée sur la littérature existante (p. 1, 8, 13, 19). La base peut aussi être le meilleur système en place (p. 8). Le principe y est donc posé pour juger les prédictions d'un système. Deux réserves. Ce qu'on juge est un prédicteur, pas une découverte isolée. Et la comparaison des règles découvertes aux modèles existants est une perspective, pas un test (p. 4, 21, 23). |
| i | **trouvée** | Des proposeurs modèles de langue optimisent le système : GEPA, où un modèle de langue révise la consigne par mutation réflexive (p. 17), et ACE, où un générateur, un réflecteur et un curateur ajoutent ou modifient des règles (p. 18-19). Ils proposent des consignes et des règles qui améliorent un prédicteur, pas des hypothèses jugées une à une. |
| ii | **trouvée en partie** | Le nul est une régression ajustée sur les contrôles connus. Dans l'évaluation (éq. 3 et 11, p. 8 et 16), ce sont des combinaisons linéaires ajustées sur l'échantillon d'évaluation. Dans la boucle (éq. 9-10, p. 16), l'optimiseur vise les résidus laissés par la loi connue ajustée sur l'entraînement. En revanche, l'archive se réduit à un seul déterminant connu (la surprise). L'option « meilleur système en place » est nommée (p. 8) mais pas appliquée. Les règles admises par le système (le livre de règles d'ACE) ne sont jamais versées dans le nul : il n'y a pas de mise en commun ajustée des lois prédictives d'une archive qui grandit. |
| iii | **non trouvée dans les pages lues** | Aucune occurrence de e-value, anytime ni sequential au sens statistique. L'inférence passe par des intervalles de confiance à 99 % par rééchantillonnage sur 1 000 tirages, à échantillon fixé (p. 13, notes des tableaux p. 32-37). Les règles d'admission sont heuristiques : gain sur mini-lot (GEPA, p. 17), règle gardée ou révisée selon la performance (ACE, p. 18). L'apprentissage en continu n'est évoqué que comme possibilité (p. 11). |
| iv | **trouvée en partie** | Sur le temps réel : consignes, contexte et paramètres sont fixés avant l'annonce (p. 3). Le banc d'essai est gelé avant le trimestre (p. 11). Les prédictions sont recueillies dans une fenêtre fixée, avant que le rendement de l'annonce n'existe (p. 1, 11). Pour la statistique hors des agents : elle est calculée par les auteurs, et la compétition annoncée enregistre les prédictions en temps réel (p. 22). Manques dans les pages lues : aucun scellement par empreinte ni horodatage (zéro occurrence de commit et timestamp). Pour les systèmes optimisés, qui portent le résultat principal (près de 20 %), le texte ne dit pas que les prédictions sur la seconde moitié du trimestre ont été émises avant les événements : le découpage se fait à la date médiane et les prédictions sont générées après l'optimisation (p. 16). Enfin, une note de la p. 12 signale qu'un des modèles a traité les transcriptions avec retard. |

Citations :

| id | page | composante | citation (texte de `pdftotext`, espaces réduits) | ce qu'elle établit |
|---|---|---|---|---|
| K01 | 1 | iv | « We introduce a real-time, out-of-sample benchmark to sidestep both problems that measures how well AI systems explain contemporaneous stock returns around earnings announcements using only information available at announcement time. » | Le banc d'essai évalue en temps réel et hors échantillon, avec la seule information disponible au moment de l'annonce : la prédiction est faite avant que le rendement de l'annonce existe. |
| K02 | 1 | P | « the best-optimized systems more than double the explained variation in returns relative to existing literature. » | Le résultat principal est donné par rapport à la littérature existante, pas par rapport à l'absence d'effet. |
| K03 | 3 | iv | « the AI model uses to make its forecasts (as well as the model parameters), are determined prior to the earnings announcement. » | Le contexte, les consignes et les paramètres du modèle sont fixés avant l'annonce : c'est un engagement avant l'observation, sans scellement par empreinte décrit. |
| K04 | 8 | ii | « Xi,t is a vector of known, quantitative determinants of the idiosyncratic market reaction (such as the standardized unexpected earnings, or SUE) » | Les contrôles de la régression d'évaluation sont des déterminants déjà connus (la surprise de bénéfice standardisée) : c'est un nul formé de ce qui est connu, mais pas une mise en commun de lois prédictives d'une archive. |
| K05 | 8 | P | « The primary performance statistic is the incremental explanatory power, or ∆R2 , generated by the AI system’s predictions over a baseline model, e.g., one that includes only the quantitative controls Xi,t or the current “best” system. » | La statistique principale est le gain d'explication au-delà d'une base faite des contrôles connus ou du meilleur système en place : c'est le principe de P, posé comme critère du banc d'essai. L'option « meilleur système en place » est nommée mais pas mise en œuvre dans les résultats. |
| K06 | 13 | P | « regressing percentile-ranked abnormal returns on the percentile-ranked earnings surprise alone yields an R2 of 5.0%, consistent with the upper end of estimates in the existing literature. » | La base d'évaluation est la surprise de bénéfice seule, recalée sur la littérature existante. |
| K07 | 13 | P | « the full-sample R2 of 0.05 serves as our primary benchmark for evaluating AI models. » | Les systèmes sont jugés contre l'explication que fournit déjà la variable connue. |
| K08 | 14 | ii | « the coefficient on the surprise remains large and highly significant for all three models » | La régression conjointe ajuste ensemble la prédiction du modèle de langue et la variable connue : c'est une combinaison linéaire ajustée avec un seul déterminant connu, pas avec une archive. |
| K09 | 19 | P | « The R2 of 17.1% represents more than a threefold improvement over the surprise-only baseline » | Le meilleur système optimisé est présenté par son gain sur la base des connaissances existantes. |
| K10 | 22 | P | « This follows a broader tradition in asset pricing to benchmark asset pricing models by their ability to explain differences in average returns. » | Les auteurs rattachent leur banc d'essai à la tradition qui juge les modèles contre des bases. |
| K11 | 16 | ii | « First, we estimate the baseline regression model strictly over the training set: » | Dans la boucle d'optimisation, la loi connue (régression sur les contrôles) est ajustée sur l'échantillon d'entraînement avant toute proposition. |
| K12 | 16 | ii | « We then extract the residuals, uk , which represent the portion of the abnormal returns unexplained by the controls. In the second stage, we optimize the prompt p by minimizing the mean squared error (MSE) between the AI system’s predictions and these residuals. » | L'optimiseur vise ce que les contrôles connus laissent inexpliqué : « au-delà du connu » est un objectif de la boucle, pas une règle de promotion. L'archive se réduit à un seul déterminant, et les règles qui survivent n'y sont pas versées. |
| K13 | 17 | i | « An LLM then reads the current prompt alongside these diagnostics and proposes a targeted revision, i.e., “reflective mutation.” » | GEPA : le proposeur est un modèle de langue qui révise la consigne. |
| K14 | 18 | i | « A Reflector module then analyzes this record, identifies patterns in errors and successes, and proposes targeted additions or modifications » | ACE : un module modèle de langue propose des règles nouvelles ou modifiées. |
| K15 | 18 | iii | « new rules are appended, existing rules are updated based on whether they improved or degraded performance » | Une règle d'ACE est admise ou révisée selon qu'elle améliore ou dégrade la performance : c'est un critère heuristique, pas une preuve séquentielle. Le livre de règles est une archive interne qui grandit, mais elle sert de contexte, pas de nul. |
| K16 | 17 | iii | « If the revised prompt improves performance on the mini-batch, it enters the candidate pool; otherwise it is discarded. » | La règle de promotion de GEPA est un gain sur un mini-lot, sans test statistique ni validité à tout instant d'arrêt. |
| K17 | 17 | iii | « returns the candidate with the highest average score on a held-out evaluation set. » | La sélection finale est le meilleur score moyen sur un ensemble mis de côté, pas un e-processus. |
| K18 | 13 | iii | « with 99% bootstrap confidence intervals in brackets. » | L'inférence se fait par intervalles de confiance par rééchantillonnage, à échantillon fixé. |
| K19 | 17 | iii | « The 99% bootstrap confidence intervals for the baseline [0.06, 0.16] and optimized [0.08, 0.19] specifications overlap » | Le gain de l'optimisation sur la base est lu par recouvrement d'intervalles à taille fixée, sans aucune preuve accumulée. |
| K20 | 9 | iii | « this yields a sufficiently large sample to provide statistically powerful, real-time tests of performance differences across systems » | Les tests de différence entre systèmes sont annoncés « en temps réel », mais la méthode est l'échantillon d'un trimestre, sans validité séquentielle décrite. |
| K21 | 11 | iii | « there is no reason that this optimization and learning cannot be applied online in real-time. » | L'apprentissage en continu est évoqué comme une possibilité, sans règle de preuve séquentielle. |
| K22 | 11 | iv | « it is the first full quarter for which our production version of the benchmark was “frozen” and operational. » | Le banc d'essai est gelé avant le trimestre évalué. |
| K23 | 11 | iv | « we pass each transcript to the candidate AI systems and require predictions to be returned within a fixed time window. » | Les prédictions sont recueillies dans une fenêtre fixée après la transcription : la prédiction précède la donnée de résultat, sans scellement par empreinte ni horodatage décrit. |
| K24 | 11 | iv | « Because the benchmark is evaluated in real time, there is effectively no possibility that announcement returns or post-event commentary contaminate the information set provided to any model. » | L'argument contre la fuite repose sur le temps réel, pas sur un engagement scellé. |
| K25 | 11 | iv | « our initial evaluations use the first half of a quarter to optimize AI systems, which are then applied to the second half of the quarter. » | Les systèmes optimisés sont entraînés sur la première moitié et évalués sur la seconde. Le texte lu ne dit pas que leurs prédictions sur la seconde moitié ont été émises en temps réel. |
| K26 | 16 | iv | « After identifying p∗ , we generate out-of-sample predictions, » | Les prédictions de validation sont générées après l'optimisation, sans date d'émission donnée par rapport aux événements de la seconde moitié du trimestre. |
| K27 | 16 | iv | « We split the data from calendar quarter four of 2025 into training and validation sets, i.e., Etrain and Eval , based on the median date following Section 3.3.3. » | Le découpage des données du trimestre est fait à la date médiane. Le texte ne dit pas si l'optimisation a été faite avant ou après la survenue des événements de validation. |
| K28 | 22 | iv | « Participants need only register their system with the competition on explainingmarkets.ai to receive programmatic access to (i) a common EA calendar and (ii) an opportunity to log a prediction in real-time when an EA occurs. » | La compétition annoncée enregistre les prédictions en temps réel, et l'évaluation commune est tenue par les organisateurs : statistique calculée hors des systèmes candidats. |
| K29 | 4 | P | « optimized agentic systems generate candidate determinants of realized returns that can be compared to the drivers of realized returns in asset pricing models. » | Comparer les déterminants découverts aux modèles existants est présenté comme une implication, pas comme un test mené. |
| K30 | 23 | P | « These learned rules can be compared to the drivers of realized returns in existing asset pricing models to potentially identify missing sources of variation » | Dans la conclusion, juger les règles découvertes contre les modèles existants reste une perspective, pas une procédure appliquée. |
| KO1 | 11 | (ajout du vérificateur) | « This enables us to collect data, generate predictions, and evaluate results strictly out of sample. » | Appuie directement la composante (iv) sur la partie temps réel : prédictions générées avant le résultat, sur un banc gelé. Elle renforce la ligne « trouvée en partie » et affaiblit la lecture « le texte ne dit pas ». Elle ne contient ni scellement par empreinte ni horodatage. |
| KO2 | 11 | (ajout du vérificateur) | « this strict temporal protocol applies at the observation level. Thus, information learned earlier in a given evaluation period can—and likely should —be used when making predictions later in the period. » | Le protocole temporel strict vaut observation par observation, y compris pour les systèmes optimisés sur la première moitié du trimestre. Cela rend probable, sans l'établir, que les prédictions de la seconde moitié soient émises en temps réel. Le « non-dit » de la lecture sur les systèmes optimisés doit donc être nuancé : le texte l'indique par le protocole, sans date d'émission explicite. |
| KO3 | 8 | (ajout du vérificateur) | « which we are exploring in ongoing work. » | Mineur : les auteurs annoncent une extension du banc à d'autres événements. Cela s'ajoute à la réserve sur les versions futures (p. 3). Aucun effet sur les statuts. |

## 4. Vérification adverse (autre modèle)

| pièce | citations rejouées | conformes | statuts réfutés | oublis décisifs ajoutés | verdict |
|---|---|---|---|---|---|
| LIU | 50 | 50 | 0 | 3 (L O1 à L O3, section 2) | **tient** |
| KL | 30 (citations du lecteur ; la correspondance n'existe que pour LIU, d'où 50 rejouées pour LIU : 27 + 12 + 11) | 30 | 0 | 3 (K O1 à K O3, section 3) | **tient** |

Termes cherchés en plus par les vérificateurs, sans occurrence utile : pour LIU, « betting », « always valid », « stopping time »,
« ensemble », « stacking », « lasso », « ridge », « commit », « seal », « ledger », « timestamp » (« posterior » et « Bayes » relèvent de
la probabilité a posteriori du nul, à taille fixée, après la course) ; pour KL, « always valid », « pre-registration », « hash »,
« archive », « encompass », « nested », « ensemble », « stack », « timestamp » (« sequential » à la p. 30 seulement).

## 5. Profondeurs et limites

- **LIU** : Empreinte conforme à l'attendu ; 84 pages, « September, 2026 », créé le 1er septembre 2026 (pdfinfo). Lues en entier, une page à la fois avec pdftotext : p. 1-22 (résumé, introduction, littérature, section 3 sur le cadre et la boucle, section 4 sur le protocole, dont 4.6 sur la sélection et l'inférence après la recherche), p. 29-34 (section 6, validation cumulative après la recherche), p. 38-45 (fin de 7.2, 7.3, section 8 : discussion, biais d'anticipation, limites, conclusion), p. 46 (références), p. 57-58 (annexe A.2, réalisation de la boucle et contexte du modèle), p. 62-63 et 65-67 (annexes A.5 et A.6 : provenance, multiplicité, courses, tests contre les prédicteurs publiés). Lues par recherche de termes seulement, sur les 84 pages, avec leurs contextes : p. 23-28 (section 5), 35-37 (section 7.1-7.2), 47-56, 59-61, 64, 68-84 (références, tableaux, annexes A.3, A.4, A.7 à A.10, B). Contextes lus en particulier p. 37, 47, 66, 68, 70-73.
- Termes cherchés (LIU) : Sur les 84 pages (insensible à la casse, texte de chaque page remis sur une ligne) : e-value (0 page), e-process (0), anytime (0), sequential (p. 37, intertitre « Critic Feedback » sans rapport ; p. 47, titre de Holm 1979), martingale (0), out-of-sample / out of sample / out-ofsample (p. 6, 22, 29, 30, 31, 34, 43, 66 : toujours pour dire que les tests ne sont PAS hors échantillon), holdout / held-out (p. 47 seulement, titre de Dwork et al. 2015 en références), pre-regist / preregist / prespecif (p. 7, 14, 16, 23, 34, 42, 57 : catalogues, seuil et règle d'information fixés d'avance ; aucun préenregistrement), commit (0), seal (0), hash (p. 70, 71, 73 : empreinte SHA-256 du livre de codage de l'audit du mécanisme et de la critique, et empreinte de provenance des enregistrements ; aucune empreinte de prédiction), archive (29 pages), library (p. 18, 22, 30, 38, 66 : bibliothèque Chen et Zimmermann de 209 prédicteurs, et bibliothèque de facteurs de French), known (p. 6, 7, 9, 10, 16), published anomal (p. 1, 5), spanning / spanned (p. 5, 16, 22, 34, 43), horse race (27 pages), discovery loop (p. 1, 4, 7, 11, 29), feedback (22 pages), et en plus prospective, freeze / frozen, null, novelty, already, previously discovered, incremental.
- Limites dites par le lecteur (LIU) : Les citations d'avril viennent de la section 3.1 de la note : je n'ai pas rouvert le PDF d'avril pour les vérifier. Les pages 23-28, 35-37, 47-56, 59-61, 64 et 68-84 (résultats de la section 5, études de cas, références, tableaux, annexes A.3, A.4, A.7 à A.10, B) n'ont été lues que par recherche de termes. Les tableaux et figures ne rendent que des fragments par pdftotext. Le dépôt de code et l'archive lisible par machine qu'annonce l'article (p. 1, 6) n'ont pas été consultés, faute de réseau : une archive cumulative destinée aux agents futurs y est décrite, sans règle statistique dans le texte lu. « Non trouvée » veut dire non trouvée dans ces pages, à cette profondeur ; ce n'est pas un trou du champ. L'absence de test prospectif est une limite de cet article, pas une case libre. Les identifiants de modèles cités dans l'article ont été volontairement laissés hors de cette sortie. Aucun fichier écrit.
- **KL** : PDF de 39 pages, empreinte conforme à l'attendu, daté « June 30, 2026 ». Pages lues en entier par pdftotext, une page à la fois : 1 à 30 (résumé, introduction, littérature liée, section 2 sur la conception du banc d'essai, section 3 sur les données, les résultats et l'optimisation par GEPA et ACE, section 4, section 5 sur la compétition, section 6 de conclusion, références, figures 1 à 3) et 38 à 39 (annexe A, définition des variables). Pages 31 à 37 (tableaux 1 à 8) : lues jusqu'aux 80 premières lignes extraites et pour leurs notes complètes, mais les cellules des tableaux n'ont pas toutes été lues. Toutes les pages 1 à 39 ont aussi été parcourues par une recherche de termes. [v2 : le fichier en compte 30 ; « 27 » est le décompte du lecteur, écart sans effet, constat m1.] Les 27 citations ont été recopiées puis vérifiées par programme : après réduction des espaces, chacune est une sous-chaîne exacte du texte que pdftotext rend pour la page indiquée. Une première version de la citation de la p. 16 a échoué parce que le texte extrait porte un « ĝ » décomposé et le signe U+2126 pour Ω ; je l'ai raccourcie et elle a été revérifiée.
- Termes cherchés (KL) : Recherche insensible à la casse, page par page, sur le texte extrait des 39 pages. Occurrences trouvées : real-time (p. 1, 2, 6, 7, 9, 10, 11, 12, 22), « real time » (p. 2, 6, 11), out-of-sample (p. 1, 2, 3, 4, 6, 7, 10, 11, 16, 17, 22), « out of sample » (p. 6, 7, 11), look-ahead (p. 1, 2, 6, 11, 12, 22, et références), benchmark (nombreuses pages, de 1 à 23), baseline (p. 8, 9, 10, 13, 16, 17, 19, 29, puis tableaux), « existing literature » (p. 1 et 13), « earnings surprise » (nombreuses pages), R2 (nombreuses pages), « explained variation » (p. 1, 3, 23), incremental (p. 5, 8, 19, 29), spanning (p. 9 et 12, au sens « s'étendant sur », jamais au sens d'un test d'englobement de facteurs), agent (nombreuses pages), optimiz (nombreuses pages), prompt (nombreuses pages), reinforcement (p. 2, 20, 24), frozen (p. 11), « ex ante » (p. 5, 11, 13), « prior to » (p. 3, 8, 10, 11, 38), known (p. 2, 8, 39). Aucune occurrence : e-value, anytime, pre-regist, commit, timestamp, nested, encompass. « sequential » n'apparaît qu'à la p. 30, dans une règle du livre de règles d'ACE (« flat sequential »), qui parle de croissance d'un trimestre à l'autre, pas de test séquentiel.
- Limites dites par le lecteur (KL) : Les tableaux des p. 31 à 37 n'ont été lus que dans leurs premières lignes extraites et dans leurs notes : l'extraction mélange les colonnes et toutes les cellules n'ont pas été relues. Les références citées, comme GEPA, ACE et Hellum et al., n'ont pas été lues : elles pourraient porter d'autres composantes. La compétition explainingmarkets.ai et son kit de développement, que l'article annonce, n'ont pas été consultés : aucun appel réseau. Il se peut que leur règle d'évaluation, l'enregistrement des prédictions ou un éventuel horodatage aillent plus loin que le texte. Des « versions futures » de l'article sont annoncées pour d'autres trimestres (p. 3) et pourraient changer la lecture de (iv). Le moment où ont été émises les prédictions des systèmes optimisés sur la seconde moitié du trimestre n'est pas établi par le texte : c'est un non-dit, pas une absence prouvée. Les citations sont vérifiées par programme dans cette session, mais aucun fichier de vérification n'a été écrit, puisque l'écriture était interdite.
- Aucun PDF n'est lu en entier d'un bout à l'autre ; les références citées par KL (GEPA, ACE) et par LIU ne sont pas lues.

## 6. Pièces de cette lecture

`citations-ssrn-o4-v1.json`, `-v2.json`, `-v3.json` (seule la v3 fait foi) ; `rejouer_citations_ssrn_o4_v1.py` ; `rejeu-citations-ssrn-o4-v1.json`
(79 sur 86), `-v2.json` (85 sur 86), `-v3.json` (86 sur 86) ; `resultat-flux-lecture-ssrn-o4-v1.json` (sorties structurées des
quatre agents, telles que rendues).

## 7. Contre-lecture de la v1 et ce que fait la v2

Contre-lecteur : modèle H, neuf, autre modèle que l'auteur ; rapport `contre-lecture-lecture-pdf-ssrn-o4-v1.md`
(`f8d415a7e14564953df5bded1ae805e7d6dc76c850db71d2145debbcbd6e0840`) ; verdict « tient avec réserves » ; rejeu refait par lui : 86 sur 86.

| constat | classe | ce que fait la v2 |
|---|---|---|
| M1 | majeur | **accepté, vérifié par l'auteur sur la copie d'avril** (A13, p. 15 ; A14, p. 14) : l'alpha rendu au proposeur n'est pas nouveau ; sections 0, 2 (justification, L09) et N-SSRN-1 corrigées ; statut (ii) inchangé |
| m1 | mineur | accepté : décomptes dits (section 5, section 4) |
| m2 | mineur | accepté : comparaison au système non optimisé dite (K32, K33) |
| m3 | mineur | accepté : livre de règles qui grandit dit (K31), versé dans le prédicteur, non dans le nul |
| m4 | mineur | accepté : KO1, KO2 et les deux réserves sur P reprises en section 0 |
| m5 | mineur | accepté : profondeur dite avec la condition de N-067 |
| m6 | mineur | accepté : date imprimée, non date de dépôt ; comparaison avec SEADS |

Les sections 2 et 3 (tables tirées des sorties des lecteurs) gardent le texte des lecteurs ; les corrections y sont marquées « [v2 : …] ».
Le rapport de contre-lecture cite, en recopiant la p. 19 de KL, le nom d'un modèle évalué par ces auteurs : il reste sur cette branche
(règle de R-2731), à expurger avant `main` si la mère le juge.
