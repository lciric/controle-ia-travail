# Lecture entière de NMV contre O4 (juge au nul formé des lois connues) : PDF et code — v1

- **Lecteur : modèle I.** Pièce : NMV, Novy-Marx et Velikov, *AI-Powered (Finance) Scholarship*, version de travail NBER 33363 (janvier 2025). **La version de la revue (Journal of Economic Literature 64(1) : 5-37, DOI 10.1257/jel.20251821) n'est pas lue** : refusée (page de connexion, `docs/sources/pdf/lecture-o4-v3/jel-20251821/refus-jel-20251821-v1.md`). Tout ce qui suit vaut pour la version de travail et pour le code au commit relevé, non pour la revue.
- **Heures (`date -u`)** : début de session 2026-11-18T01:42:41Z ; extraction page par page 2026-11-18T01:43:06Z ; recherche de termes 2026-11-18T01:43:44Z ; rédaction de cette note commencée 2026-11-18T01:48:33Z ; rejeu final des citations et des extraits 2026-11-18T01:52:36Z.
- **PDF** : `docs/sources/pdf/lecture-o4-v2/nber-w33363/w33363.pdf`, 42 pages, sha256 `d889aff69bdcb65d232b7c3e9294c9a821417b0e8a813c85994619403302a0d3` (recalculé, conforme).
- **Code** : clone en lecture seule `AI-Powered-Scholarship`, origine https://github.com/velikov-mihail/AI-Powered-Scholarship, commit `f96cd709421caafa5323615fb04a41a3f0d28a4b` (vérifié par `git rev-parse HEAD` ; message du commit : Update to October, 2025 version, daté du 23 octobre 2025). Provenance et empreintes : `docs/sources/code/lecture-o4-v1/nmv/provenance-v1.md`. Aucun programme du clone n'a été lancé ; le dossier des 380 articles générés n'a été ni listé en détail ni ouvert (seul leur nombre a été compté).
- **Profondeurs** : PDF lu **en entier**, pages 1 à 42, aucune page sautée (section 1). Code : 11 fichiers de programme lus en entier, README lu hors tableau HTML et hors liste des références générées, LICENSE lu ; Inputs/ par nom et empreinte seulement (section 1).
- **Rejeu** : citations du PDF **44 sur 44** (`lecture-entiere-nmv-o4-v1-resultat-citations-pdf.json`, programme `verifier_citations_priorite_haute_o4_v1.py` inchangé) ; extraits de code **34 sur 34** (`lecture-entiere-nmv-o4-v1-resultat-extraits-code.json`, programme `verifier_extraits_code_o4_v1.py` inchangé, code de sortie 0).
- **Règles** : R7 (rien sans page ou lignes), R8 (*non trouvé* = non trouvé dans ce qui est lu ici, à la profondeur déclarée), R4 (doute tranché contre notre revendication), N-067 (rien n'est déclaré libre ; le verdict en vigueur sur O4 reste **occupée en partie** ; tout écart est un nœud, section 8). Pages = pages du PDF (1 = première page du fichier ; la page imprimée vaut page du PDF moins 1). Dans cette note, les guillemets français ne servent qu'aux citations de l'article, toutes dans le fichier de citations ; les accents graves marquent les noms (fichiers, fonctions, commandes, empreintes) et les extraits de code, ces derniers tous dans le fichier d'extraits ; les mots de la v2 ou de nos notes sont en italique. Le nom du modèle de langue dont les auteurs se servent pour rédiger n'est pas recopié (consigne) : je dis *un modèle de langue commercial*.

## 1. Profondeurs

**PDF (42 pages, `pdftotext -layout -f N -l N`, une page à la fois)** : pages 1 à 42 lues en entier. Contenu : p. 1 couverture NBER ; p. 2 résumé ; p. 3-8 introduction et début de la méthode ; p. 8-10 construction et crible des signaux ; p. 10-12 chaîne de rédaction par modèle de langue ; p. 12-15 résultats et discussion ; p. 15-20 intégrité, recommandations, conclusion ; p. 20-30 références (dont les entrées de l'auteur fictif « I. M. Harking », articles générés) ; p. 31 figure 1 ; p. 32 tableau 1 ; p. 33-37 annexe A (consignes données au modèle de langue : [p. 33] « This appendix details the exact prompts used to generate the papers’ content ») ; p. 38-42 annexe B, tableau 2 (liste des signaux et titres). Aucune page sautée. Les pages 20-30 et 38-42 sont des listes : lues ligne à ligne, sans contenu de méthode.

**Code (commit `f96cd709…`)**, liste par `git ls-files` : 15 fichiers hors `pdfs/` (380 fichiers dans `pdfs/`, comptés, non listés, non ouverts).

| fichier | lignes | lu |
|---|---|---|
| `1.generate_template_reports.m` | 38 | en entier |
| `2.main.py` | 336 | en entier |
| `Functions & Scripts/run_data_mining.m` | 109 | en entier |
| `Functions & Scripts/organize_results.m` | 194 | en entier |
| `Functions & Scripts/filter_results.m` | 50 | en entier |
| `Functions & Scripts/run_protocol.m` | 75 | en entier |
| `Functions & Scripts/makeSignalInfo.m` | 87 | en entier |
| `Functions & Scripts/make_data.m` | 73 | en entier |
| `Functions & Scripts/create_table1_figure4.m` | 258 | en entier |
| `Functions & Scripts/models.py` | 948 | en entier |
| `Functions & Scripts/make_figures.py` | 534 | en entier |
| `README.md` | 1562 | l. 1-120 en entier ; l. 121-1178 (tableau HTML des signaux) par filtre des seules lignes hors balises ; l. 1179-1562 en entier sauf les lignes vides et les 95 lignes de références à l'auteur fictif |
| `LICENSE` | 21 | en entier |
| `.gitattributes` | 2 | en entier |
| `Inputs/Mining_Variable_List.xlsx`, `Inputs/compustat_variable_dictionary.csv` | — | par nom et empreinte seulement (consigne) |

**Borne décisive du code** : les fonctions qui font les tests du protocole (tri univarié, test du signal, régression de recouvrement sur les anomalies proches, liste des anomalies publiées) appartiennent à la boîte à outils *Assaying Anomalies* v0.4, **qui n'est pas dans le clone** : `This code is to be used in conjunction with the MATLAB asset pricing package that accompanies Novy-Marx and Velikov (2024), Assaying Anomalies.` (README l. 1183) ; `The results in Novy-Marx and Velikov (2025) use the pre-release v0.4 of the MATLAB Toolkit.` (README l. 1191). Ce que le clone montre, c'est l'appel de ces fonctions et la règle de sélection appliquée à leurs sorties ; ce qu'elles calculent n'est pas lu.

## 2. Recherche de termes (texte entier du PDF, deux extractions : mise en page et brute, césures de fin de ligne recollées, casse ignorée)

| terme | occurrences | ce que c'est |
|---|---|---|
| *e-value*, *e-process*, *anytime*, *martingale*, *optional stopping* (et *stopping* seul), *sequential test*, *likelihood ratio*, *Bayes factor* | 0 | — |
| *encompass* | 1 (p. 12) | sens courant : « encompassing data-driven predictor identification » (la chaîne englobe…), pas un test d'englobement |
| *spanning* | 0 | mais *span* : p. 8 (sens courant) et p. 32, critère « Close Span » du tableau 1 (voir section 3) |
| *incremental* | 1 (p. 9) | « suggesting genuine incremental predictive power beyond standard factor benchmarks » |
| *marginal* | 0 | — |
| *benchmark* | 3 (p. 2, p. 9 deux fois) | « benchmarks it to more than 200 other known anomalies » (p. 2) ; p. 9, voir ci-dessus et section 3 |
| *baseline*, *null* | 0 | — |
| *multiple testing*, *false discovery*, *Bonferroni*, *Holm* | 0 | (*multiple* : 3 occurrences, sens courant, p. 6, 8, 15) |
| *pre-regist* / *preregist*, *pre-commit* / *precommit*, *seal* | 0 | — |
| *hash* | 1 (p. 30) | faux positif : « Tatsunori Hashimoto » (référence) |
| *out-of-sample* (ajouté) | 2 (p. 3, p. 19) | p. 19, recommandation : « greater emphasis on out-of-sample validation » |
| *p-hacking* (ajouté) | 2 (p. 16) | « could exponentially increase the scope of data mining and p-hacking » |

Dans le code lu (fichiers de la section 1, hors Inputs/) : *hash*, *seal*, *Bonferroni*, *Holm*, *false discovery*, *e-value*, *martingale*, *anytime*, *likelihood*, *Bayes*, *null*, *seed*, *rng*, *timestamp*, *pre-regist* : aucune occurrence ; *sha* : seulement à l'intérieur de mots (reshape, shall et autres) ; *sequential* : une fois, README l. 1402, ordre d'exécution des scripts ; *span* : les variables CloseSpan (section 4). Une recherche de termes ne trouve pas une idée écrite avec d'autres mots : les statuts reposent sur la lecture entière, non sur ce tableau.

## 3. Lecture du PDF par composante

**Ce que fait la pièce.** Une chaîne en trois temps : fouille de signaux comptables par programme, crible statistique par programme, puis rédaction d'articles par modèle de langue. [p. 2] « apply the Novy-Marx and Velikov (2024) “Assaying Anomalies” protocol to generate standardized “template reports” for 96 signals that pass the protocol’s rigorous criteria » ; [p. 2] « benchmarks it to more than 200 other known anomalies » ; [p. 2] « we use state-of-the-art LLMs to generate three distinct complete versions of academic papers for each signal ». Le but avoué est la mise en garde : [p. 2] « industrialize HARKing (Hypothesizing After Results are Known) » ; [p. 16] « our pipeline exemplifies the risk of industrialized HARKing ».

**Le crible, étape par étape.** [p. 8] « This initial dataset comprises 31,460 potential predictors » ; [p. 8] « we confine the sample period to signals available through December 2023 and require at least 360 months of historical data ». Puis une cascade cumulative de six critères, tous au même seuil, chacun sur la période historique du signal (au moins 360 mois) :
- quatre tris de portefeuilles jugés **contre zéro** (écart de rendement significatif) : [p. 9] « 7,102 (approximately 41.6%) generate statistically significant return spreads at the 5% level » ; tableau 1, [p. 32] « Panel B: Cumulative significance criteria » ;
- un alpha contre un **modèle de facteurs fixé** : [p. 9] « we next adjust each signal’s returns using the Fama and French (2018) six-factor model » ; [p. 9] « only 183 signals (1.1%) remain statistically significant » ; [p. 9] « suggesting genuine incremental predictive power beyond standard factor benchmarks » ; critère du tableau 1 : [p. 32] « + |tα̂(quintile, NYSE, VW) | > 1.96 » ;
- un test contre les **anomalies publiées proches** : [p. 9] « rigorously benchmarks each candidate predictor against the expansive “zoo” of published » [p. 10] « anomalies from Chen and Zimmermann (2022) » ; [p. 10] « The protocol automatically produces detailed PDF “template reports” for each signal » ; [p. 10] « After reviewing these results and filtering out signals that fail to demonstrate robust performance relative to closely related anomalies, we are left with only 96 signals (0.6%) » ; critère du tableau 1 : [p. 32] « + |tAssay, Close Span | > 1.96 ». La p. 10 parle d'un examen ; le tableau 1 donne la même étape comme une règle à seuil sur une statistique de Student nommée « Close Span ». Le texte ne définit pas cette statistique (ni quelles anomalies sont *proches*, ni la régression) ; la définition est dans la boîte à outils, non lue.

**P. Juger contre le connu, non contre *aucun effet*.** Les deux derniers critères jugent chaque signal contre le connu : un modèle à six facteurs (p. 9, 32), puis les anomalies publiées les plus proches tirées d'une archive de plus de 200 anomalies (p. 2, 9-10, 32). Les quatre premiers critères sont contre zéro. Le jugement est fait par programme : [p. 5] « all empirical analyses and statistical validations are conducted using rigorous methods developed in the academic literature » ; [p. 10] « The protocol automatically produces detailed PDF “template reports” for each signal ». Il porte sur des signaux minés, **non sur des propositions du modèle de langue**. → **pris, hors modèle de langue.**

**(i) Proposeurs modèles de langue.** Le modèle de langue n'intervient qu'après le crible : [p. 10] « leverages state-of-the-art large language models » pour rédiger, à partir des rapports du protocole ; il nomme les signaux, puis écrit les hypothèses : [p. 11] « Proposes economic mechanisms justifying the signal’s predictive power » ; [p. 5] « contain different hypotheses and economic » « explanations ». Les auteurs disent ces hypothèses *testables* mais ne les testent pas : [p. 13] « Develops testable hypotheses that align with the empirical results » ; [p. 7] « use AI to generate testable hypotheses explaining the findings » ; l'évaluation de l'accord entre hypothèses et résultats est **projetée**, et manuelle : [p. 14] « We are currently working on a systematic evaluation » ; [p. 14] « we will manually extract the main hypotheses stated in the introduction and compare it against the key statistical findings ». La consigne donnée au modèle lui fait recopier les résultats : [p. 34] « Mirror exactly the terminology used in the results section » ; la conclusion part du résumé : [p. 37] « The conclusion should be based on the following abstract ». L'introduction de l'article place l'ensemble « from hypothesis generation through full paper creation » (p. 4), mais la *génération d'hypothèses* y est l'écriture d'une justification après coup, et la discussion le dit : [p. 15] « AI enables rapid iteration between empirical discovery and theoretical justification » ; c'est ce que pose la question de la p. 3 : « Should it matter if an AI system generated these hypotheses after seeing the results? ». → **voisin** : le modèle de langue écrit des hypothèses, après le résultat, et rien de ce qu'il écrit n'est testé.

**(ii) Nul = mise en commun ajustée des lois prédictives de l'archive.** Le dernier critère compare chaque signal aux anomalies publiées les plus proches, prises dans une archive (p. 9-10) : c'est un nul formé de lois connues, sous forme d'une statistique de recouvrement (« Close Span », p. 32). Ce qui manque, dans le texte lu : l'archive est **fixe** (anomalies publiées), elle ne reçoit pas les signaux admis par la chaîne elle-même ; la forme du nul (quelles anomalies, combien, quelle régression, quelle mise en commun) n'est pas écrite dans le PDF ; ce ne sont pas des lois prédictives comparées par vraisemblance. → **voisin** (proche : nul formé de l'archive publiée, en régression ; voir le nœud 1).

**(iii) e-processus comme règle de promotion.** La règle est une cascade de seuils fixes, |t| > 1,96 à chaque étape, sur un échantillon fixé (p. 9, 32), sans correction pour les 17 074 candidats testés (aucune occurrence de *multiple testing*, *false discovery*, *Bonferroni*, *Holm*, section 2) ; les auteurs nomment le risque sans le corriger : [p. 16] « could exponentially increase the scope of data mining and p-hacking ». Aucun terme d'e-valeur, d'e-processus ou de validité à tout instant d'arrêt. → **non trouvé.**

**(iv-a) Prédictions engagées avant que les données existent.** Les données existent avant tout (échantillon jusqu'à décembre 2023, p. 8 ; tableau 1, [p. 32] « Require data until 12/2023 » et « Require 360 months ») ; le modèle de langue écrit après le résultat, par construction (p. 2, 3, 16). L'engagement d'avance n'apparaît qu'en recommandation : [p. 19] « Economic stories justifying observed phenomena should be evaluated, at least in part, by the novel testable predictions they make beyond the primary findings they were designed to explain » ; [p. 19] « greater emphasis on out-of-sample validation ». Aucun scellement, aucune empreinte (section 2). → **non trouvé** (la pièce est l'exemple inverse : HARKing industrialisé, revendiqué comme mise en garde).

**(iv-b) Statistique calculée hors des agents.** Toute la statistique est calculée par programme, avant et hors du modèle de langue (p. 5, 10, 12 : [p. 12] « The final assembly relies on custom scripts ») ; mais elle juge des signaux minés, non des propositions d'agents. → **voisin** (comme en v2).

## 4. Lecture du code (commit `f96cd709421caafa5323615fb04a41a3f0d28a4b`)

**Version.** Le code est d'octobre 2025, postérieur à la version de travail lue (janvier 2025) : `standardized "template reports" for 95 signals that pass the protocol's rigorous` (README l. 6) et `generate **four distinct**` (README l. 9), contre 96 signaux et trois versions dans le PDF (p. 2) ; fin d'échantillon `emonth_cutoff = 202412;` (filter_results.m l. 13) contre décembre 2023 dans le PDF (p. 8, 32). Le code ne rejoue donc pas exactement la course décrite par la version de travail ; il décrit probablement celle d'une version ultérieure (non lue : la revue est refusée). Ce qui suit vaut pour ce commit.

**Chaîne.** `1.generate_template_reports.m` enchaîne fouille, organisation, filtre et protocole : `run('run_data_mining.m');` (l. 26) ; `run('filter_results.m'); %% Run protocol on filtered signals run('run_protocol.m');` (l. 34-38). Aucun modèle de langue dans cette partie.

**Évaluation et statistique (par programme, hors modèle de langue).**
- Tri et régression contre six facteurs dès la fouille : `tempRes = runUnivSort(ret, ind, dates, me, 'timePeriod', 196307, ... 'weighting', weight, ... 'factorModel', 6,` (run_data_mining.m l. 88-90 ; `runUnivSort` est dans la boîte à outils, non lue).
- Échantillon fixé : `s = find(dates==196307); e = find(dates==202412);` (organize_results.m l. 37-38).
- Rendement contre zéro : `tmpRes = ols(pret, const(s:e)); results.xret(count) = tmpRes.beta; results.txret(count) = tmpRes.tstat;` (l. 125-127) ; alpha contre le modèle à six facteurs : `tmpRes = ols(pret, ff6(s:e,:)); results.alpha(count) = tmpRes.beta(1); results.talpha(count) = tmpRes.tstat(1);` (l. 130-132).

**Règle de sélection.** Seuil unique, sans correction de multiplicité : `t_cutoff = 1.96; cmonth_cutoff = 360; emonth_cutoff = 202412;` (filter_results.m l. 11-13) ; conjonction des critères : `abs(res.txret)>t_cutoff & abs(res.txret2)>t_cutoff & abs(res.txret3)>t_cutoff & abs(res.txret4)>t_cutoff & abs(res.talpha4)>t_cutoff` (l. 47). Quatre critères contre zéro, un contre six facteurs : le code confirme la structure du texte.

**Comparaison au connu (archive).** `[anoms, labelsCZ, anomaly_summary] = getChenZimmermanAnomalies();` (run_protocol.m l. 26) ; `runTestSignal(signalInfo(i), anoms, labels, resAnoms);` (l. 42) ; la statistique retenue : `finalRes.CloseSpanT(i) = ResStruct.resCloseSpan(7).tstat(1);` (l. 66) ; la sélection finale, mécanique : `temp = finalRes(abs(finalRes.CloseSpanT)>1.96,{'numer','denom','signal','varName'}); filePath = [pwd,filesep,'tex',filesep,'signals.csv']; writetable(temp, filePath);` (l. 73-75). Donc, à ce commit, l'étape « After reviewing these results » de la p. 10 est une règle à seuil par programme, comme le dit le tableau 1 (p. 32) ; je ne peux pas exclure, sur pièce, un examen humain en plus lors de la course de janvier 2025. Ce que désigne l'indice 7 de `resCloseSpan`, quelles anomalies sont *proches* et quelle régression est faite : dans `runTestSignal`, boîte à outils non lue.

**Le modèle de langue n'est en aval que du crible ; rien de ce qu'il écrit ne revient à un test.** Le programme Python lit la sortie du filtre : `signals_csv_path = os.path.join(args.base_dir, args.signals_csv)` (2.main.py l. 258), puis rédige chaque version : `generator.process_version( signal=signal, version=version_idx, cleaned_text=cleaned_text, hypothesis_type=hypothesis_type, file_tag=tag, )` (l. 324-330) ; `introduction_sections, bib_entries = self.generate_intro( signal.signal_name, cleaned_text, hypothesis_type=hypothesis_type )` (models.py l. 375-377) ; le modèle reçoit le rapport du protocole : `Base the results section strictly on the following data, matching its terminology and precision: {kwargs['modified_latex']}` (l. 536-537) ; il écrit des mécanismes : `2. Hypothesis Development (3 paragraphs, ~300 words total): - Present economic mechanisms linking the signal to returns` (l. 506-507) ; version libre : `LLM proposes economic mechanisms organically` (README l. 1278) ; la sortie va au fichier LaTeX : `with open(output_file_path, 'w', encoding="utf-8") as file: file.write(modified_latex)` (models.py l. 866-868). Aucun chemin de la sortie du modèle vers un calcul statistique dans les fichiers lus ; `make_figures.py` ne fait que des figures : `Combined script to generate all paper figures: 1. PDF grid thumbnail 2. Readability box plots (FKI and GFI) 3. Sankey diagram` (l. 5-8).

**Engagement, scellement, empreinte.** Aucun stockage de prédiction avant l'issue, aucune empreinte, aucune graine (section 2). Le sens du signal est choisi **après** avoir vu le rendement : `if res.xret(end)<0 var = - var; numer = ['neg_', numer]; end` (makeSignalInfo.m l. 57-60). Un bruit sans graine fixée est ajouté aux signaux : `var = var+randn(size(me))*1e-12;` (run_data_mining.m l. 61 ; même ligne dans makeSignalInfo.m l. 47, non extraite) — sans portée pour O4, noté pour la reproductibilité.

**Écarts du code avec le texte (R4, constats, non jugés).**
1. Dénombrements et période (ci-dessus) : 95 signaux et quatre versions, fin 2024, contre 96, trois, fin 2023.
2. Spécification des quatre tris : le tableau 1 du PDF commence par un tri en déciles, points de coupure de l'échantillon, poids égaux (p. 32) ; le filtre du code commence par `% Step 1: Quintile, NYSE-breaks, EW` (filter_results.m l. 16-20). Dans `create_table1_figure4.m`, le premier filtre calculé est `% S1: quintile, NYSE, EW` (l. 82-84) et la ligne affichée à la console dit `'+ |t_r(quintile, NYSE, EW)| > 1.96'` (l. 110), mais l'étiquette écrite dans le tableau LaTeX dit `(decile, name, EW)` (l. 159) : à ce commit, les étiquettes du tableau LaTeX ne décrivent pas les filtres calculés. Je ne tranche pas laquelle des deux descriptions vaut pour la course de la version de travail.
3. La figure compare `indFin = (finalRes.CloseSpanT)>1.96;` (create_table1_figure4.m l. 209), sans valeur absolue, alors que la sélection prend la valeur absolue (run_protocol.m l. 73) ; sans portée pour O4.
4. Le code confirme le texte sur ce qui compte pour O4 : crible par programme ; seuil 1,96 à chaque étape ; aucune correction de multiplicité ; alpha contre six facteurs ; statistique de recouvrement contre les anomalies proches au seuil 1,96 ; modèle de langue en aval, sans retour.

## 5. Réponses aux questions propres à la pièce

1. **Le crible juge-t-il chaque signal contre des facteurs connus ou contre zéro ?** Les deux, en cascade : quatre critères contre zéro (rendement d'écart), puis un alpha contre le modèle à six facteurs de Fama et French (p. 9, 32 ; organize_results.m l. 130-132 ; filter_results.m l. 47), puis une statistique de recouvrement contre les anomalies publiées proches (p. 9-10, 32 ; run_protocol.m l. 66, 73). La définition de cette dernière est hors du PDF et hors du clone.
2. **Calculé par programme ?** Oui (p. 5, 10 ; code MATLAB, section 4). Le cœur des tests est dans la boîte à outils *Assaying Anomalies* v0.4, non lue (README l. 1183, 1191).
3. **Règle, seuil, correction de multiplicité ?** Conjonction de seuils |t| > 1,96 (5 %), un par étape, sur un échantillon fixé (1963-2023 dans le texte, 1963-2024 au commit lu) ; aucune correction de multiplicité dans le texte ni dans le code ; l'article ne présente pas la cascade comme un contrôle d'erreur.
4. **Le modèle de langue propose-t-il quoi que ce soit qui soit ensuite testé ?** Non dans ce qui est lu : il nomme les signaux et écrit des hypothèses après le crible ; l'évaluation de l'accord hypothèses-résultats est annoncée, manuelle, non faite (p. 14) ; le code n'a aucun chemin de retour (section 4).
5. **Engagement avant les données, e-valeur, validité à tout instant d'arrêt ?** Aucun des trois (section 2 et 3) ; l'engagement n'apparaît qu'en recommandation (p. 19). Le sens du signal est même choisi après coup (makeSignalInfo.m l. 57-60).
6. **Le code confirme-t-il ou contredit-il le texte ?** Il confirme la structure (section 4, point 4), à un commit postérieur dont les dénombrements, la période et la spécification des tris diffèrent de la version de travail (section 4, écarts 1 et 2). Il confirme aussi que la dernière étape est, à ce commit, une règle à seuil par programme, ce que le tableau 1 (p. 32) disait déjà et que la p. 10 (« After reviewing these results ») laissait ouvert.

## 6. Table *pris, voisin, non trouvé* de cette pièce

| composante | statut | preuve |
|---|---|---|
| **P** | **pris, hors modèle de langue** | alpha contre six facteurs (p. 9, 32 ; organize_results.m l. 130-132 ; filter_results.m l. 47) ; recouvrement contre les anomalies publiées proches (p. 9-10, 32 ; run_protocol.m l. 26, 42, 66, 73) ; sur des signaux minés |
| **(i)** | **voisin** | le modèle de langue écrit des hypothèses après le résultat (p. 5, 11, 13) ; rien n'est testé (p. 14 ; 2.main.py l. 258, 324-330 ; models.py l. 536-537, 866-868) |
| **(ii)** | **voisin (proche)** | nul formé d'une archive publiée (zoo de Chen et Zimmermann), statistique « Close Span » (p. 9-10, 32 ; run_protocol.m l. 26, 66) ; archive fixe, sans les admis de la chaîne ; forme du nul non écrite dans le PDF, non lue dans le code (boîte à outils) |
| **(iii)** | **non trouvé** | seuils fixes |t| > 1,96 (p. 32 ; filter_results.m l. 11, 47 ; run_protocol.m l. 73) ; termes à zéro (section 2) |
| **(iv-a)** | **non trouvé** | données antérieures (p. 8, 32) ; HARKing revendiqué (p. 2, 16) ; recommandation seulement (p. 19) ; sens choisi après coup (makeSignalInfo.m l. 57-60) |
| **(iv-b)** | **voisin** | statistique par programme (p. 5, 10, 12 ; section 4), mais sur des signaux minés, non sur des propositions d'agents |
| **conjonction** | **non trouvée dans cette pièce** | ni (iii) ni (iv-a) ; (i) seulement après coup |

## 7. Changements par rapport à la v2 (`lecture-pdf-priorite-haute-o4-v2.md`, section 3.6 et lignes NMV des sections 2 et 4)

| constat | v2 | cette lecture | change ? |
|---|---|---|---|
| Profondeur PDF | p. 5, 9, 10, 11 en entier ; p. 2 par lignes filtrées ; *p. 1-2, 4-5, 8-10, 14, 18, 32* déclarées en v1 | **p. 1-42 en entier** | oui |
| Code | non lu | lu (section 1), commit `f96cd709…` | oui |
| Termes | e-value, e-process, anytime, martingale, stopping, sequential test, likelihood ratio : aucune occurrence | confirmé, et liste étendue (section 2) : aucune occurrence de *null*, *baseline*, *multiple testing*, *false discovery*, *Bonferroni*, *Holm*, *pre-regist*, *pre-commit*, *seal* ; *hash* faux positif | non sur le fond ; précisé |
| P | pris, hors modèle de langue ; tri contre six facteurs puis plus de 200 anomalies ; taille fixée 5 % | **inchangé** ; précisé : quatre critères sur six sont contre zéro ; les deux derniers contre le connu (p. 32, tableau 1, non cité en v2) ; confirmé par le code | statut non ; précision oui |
| Dernière étape, *qui examine* | *la page ne dit pas qui examine* ; *filtre humain* retiré | la p. 10 reste muette ; mais le tableau 1 (p. 32) donne une règle à seuil « + |tAssay, Close Span | > 1.96 », et le code l'applique mécaniquement (run_protocol.m l. 73), à un commit postérieur | oui (précision) |
| (i) | voisin (hypothèses écrites après le signal, p. 5, 11) | **inchangé** ; ajouté : l'accord hypothèses-résultats n'est pas testé, évaluation projetée et manuelle (p. 14) ; aucun chemin de retour dans le code | statut non |
| (ii) | NMV absent de la ligne (ii) (*dans aucune des six pièces lues* pour *pris* ; NMV non cité parmi les voisins) | **voisin (proche)** : nul formé de l'archive publiée, en statistique de recouvrement (p. 9-10, 32 ; run_protocol.m l. 66) | **oui** (nœud 1) |
| (iii) | NMV non cité sur la ligne (iii) | **non trouvé**, avec la règle exacte : |t| > 1,96 par étape, sans correction (p. 32 ; filter_results.m l. 11, 47) | oui (précision) |
| (iv-a) | NMV non cité ; *sans engagement trouvé dans les pages lues* | **non trouvé** à la lecture entière ; engagement seulement recommandé (p. 19) ; sens du signal fixé après coup (code) | oui (profondeur) |
| (iv-b) | voisin (crible par programme, pas des propositions de modèle de langue) | **inchangé**, confirmé par le code | non |
| Version de la revue | non lue | non lue : refusée (page de connexion) ; le code lu correspond à une version ultérieure à la version de travail (95 signaux, quatre versions, fin 2024) | oui (nouveau fait) |
| Écarts code-texte | sans objet | spécification des tris et étiquettes du tableau LaTeX non concordantes à ce commit (section 4, écart 2) | oui (nouveau) |

Ce qui ne change pas : NMV ne touche pas la conjonction ; le verdict en vigueur sur O4 (**occupée en partie**) n'est ni contredit ni élargi par cette pièce au-delà du nœud 1 ; la citation de la v2 « contain different hypotheses and economic » (p. 5) et celle des 183 signaux (p. 9) se rejouent telles quelles.

## 8. Nœuds pour Lazar (décisions à prendre, non des conclusions)

1. **NMV et (ii).** La note d'englobement crédite SEADS de (ii) *sous forme de régression*. NMV juge chaque signal survivant contre les anomalies publiées les plus proches, tirées d'une archive de plus de 200 anomalies, par une statistique de recouvrement à seuil (p. 9-10, 32 ; run_protocol.m l. 26, 66, 73), pour une recherche par programme, sans modèle de langue dans le crible. Décision : porter NMV comme voisin de P et de (ii) dans la note d'englobement (archive fixe, nul hors boucle, forme non lue), et dire ou non que la partie *lois connues* de (ii), sous forme de régression, est publiée dès janvier 2025 hors modèle de langue. Par R4, je recommande de l'écrire.
2. **Ligne NMV dans la table des pièces.** Proposition de libellé, en italique : *occupe le principe hors modèle de langue (crible par programme contre six facteurs puis contre les anomalies publiées proches, |t| > 1,96 sans correction, échantillon fixé) ; le modèle de langue n'écrit qu'après coup, sans test ; ni e-processus, ni engagement*. Décision : l'ajouter, et retirer NMV de la liste des pistes non lues de priorité haute (point 5) pour la version de travail seulement.
3. **Version de la revue.** JEL 64(1) refusée ; le code au commit lu décrit une course plus récente que la version de travail. Décision : fournir le PDF de la revue (ou une version SSRN 5060022 / 5103553), ou ne citer publiquement que NBER 33363 et le code au commit `f96cd709…`. Tant que la revue n'est pas lue, rien ne peut être dit sur ce qu'elle ajoute (par exemple une évaluation des hypothèses).
4. **Boîte à outils *Assaying Anomalies* v0.4.** La forme exacte du nul de l'étape finale (anomalies retenues comme proches, régression, indice 7 de `resCloseSpan`) n'est lisible que dans ce code, absent du clone. Décision : le faire relever (clone à fournir, aucun accès réseau ici) ou garder la réserve *forme non lue*.
5. **Usage comme contre-exemple.** NMV met en scène l'inverse de (iv-a) (HARKing industrialisé, p. 2, 16) et recommande l'évaluation par prédictions nouvelles (p. 19). Décision : le citer ou non comme motivation publiée de (iv-a) dans la lettre de O4 (citation obligatoire au sens de N-067).

## 9. Ce qui reste non lu

- Version de la revue (JEL 64(1) : 5-37), refusée ; versions SSRN 5060022 et 5103553, non tentées (SSRN refuse ce poste, voir le fichier de refus).
- Boîte à outils *Assaying Anomalies* v0.4 (fonctions `runUnivSort`, `runTestSignal`, `getChenZimmermanAnomalies`, `makeAnomStratResults`, `calcGenAlpha`, `ols`) : absente du clone.
- Les 380 articles générés (`pdfs/`), non ouverts (consigne) ; les rapports du protocole (sorties) ne sont pas dans le clone lu.
- Contenu de `Inputs/` (par nom et empreinte seulement) ; dans README, le corps du tableau HTML (l. 121-1178) hors lignes de texte, et les 95 lignes de références à l'auteur fictif.
- Le balado et la page SSRN cités par le README, non consultés (aucun accès réseau).

## 10. Incidents et refus, tels quels

- Aucun refus de permission, de crochet ou de classifieur pendant cette lecture.
- Premier rejeu d'essai des citations (fichier provisoire, hors dépôt) : 38 sur 40 ; deux citations de la p. 32, formées chacune d'un seuil suivi d'un dénombrement, échouaient parce que l'extraction brute de `pdftotext` sépare les colonnes du tableau 1. Corrigé **sur la source** : remplacées par les libellés de lignes du tableau tels qu'ils sont extraits ; programme de rejeu inchangé. Rejeu final : 44 sur 44 (trois citations ajoutées ensuite pour couvrir des mots cités entre guillemets) ; extraits : 34 sur 34 (dont deux lignes du fichier de licence, citées dans la provenance : `MIT License`, `Copyright (c) 2024 velikov-mihail`).
- Le PDF (p. 5, 11, 13), le README et `2.main.py` nomment des modèles de langue commerciaux ; ces noms ne sont pas recopiés ici (consigne), et aucun extrait versé ne les contient.
- Le programme de rejeu des citations compare les seuls caractères alphanumériques, casse ignorée (défaut déjà dit en v2) ; non modifié.
