# Lecture de la piste nouvelle AA (boîte à outils *Assaying Anomalies* v0.4.0) contre O4 — v1

- **Lecteur** : modèle I (session du compte organisme), processeur seul, sans réseau.
- **Heures (`date -u`)** : début 2026-11-18T03:07:28Z ; fin 2026-11-18T03:18:03Z.
- **Pièce lue par son code seulement.** L'article (Novy-Marx et Velikov, *Assaying Anomalies*, SSRN 4338007) n'est pas lu : accès refusé, voir `docs/sources/pdf/lecture-o4-v3/ssrn-4338007/refus-ssrn-4338007-v1.md`. Aucun PDF n'est cité ; la liste des citations PDF est vide (`lecture-piste-nouvelle-aa-o4-v1-citations-pdf.json`, 0 sur 0).
- **Source** : clone en lecture seule `code-o4/AssayingAnomalies` (origine `https://github.com/velikov-mihail/AssayingAnomalies`), commit `f08a77f7f98bfec8de893effb8bd4f5524dbbb48`, étiquette `v0.4.0`, clone superficiel (un seul commit), 1 410 fichiers suivis ; empreintes des fichiers lus dans `docs/sources/code/lecture-o4-v1/aa/provenance-v1.md`. Pour la question 3, le clone `code-o4/AI-Powered-Scholarship` au commit `f96cd709421caafa5323615fb04a41a3f0d28a4b`.
- **Rejeux** : extraits de code **53 sur 53** (`lecture-piste-nouvelle-aa-o4-v1-resultat-extraits-code.json`) ; citations PDF **0 sur 0** (`lecture-piste-nouvelle-aa-o4-v1-resultat-citations-pdf.json`). Chaque passage entre guillemets ci-dessous est un extrait de code rejoué, repéré par sa clé [Exx] ou [Pxx] dans le JSON des extraits.
- **Condition de proportion** : README et point d'entrée lus d'abord ; la pièce touche P et (ii) dès le README et `runTestSignal.m` ; lecture poursuivie (section 1).

## 1. Profondeur

**Lus en entier** (clone AA) : `README.md`, `test_signal.m`, `LICENSE`, `Functions/Assay functions/runTestSignal.m`, `makeCloseAnomResults.m`, `makeAnomStratResults.m`, `checkFillAnomalies.m`, `makeAnomBenchmarkResults.m`, `makeBasicSortsResults.m`, `makeCombStrats.m`, `Functions/Asset pricing/getChenZimmermanAnomalies.m`, `Functions/Utilities/nanols.m`, `calcPanelCorrels.m`, `Functions/Utilities/jplv7/regress/ols.m` (l. 1-79, le reste est l'impression des résultats non lue).

**Lus par plages** : `makeResToPrint.m` (l. 40-55, 160-260, 360-460, plus recherche de `close`, `span`, `tstat`, `comb`) ; `makeFMBRes.m` (l. 30-102) ; `prt/printCloseAnomsSection.m` (l. 36-127) ; `prt/printCombStratsSection.m` (l. 36-76) ; `prt/printTitlePage.m` (l. 58-85) ; `prt/printTexFile.m` (l. 60-78) ; `prt/printOtherAnomaliesSection.m` (l. 36-94, par recherche) ; `prt/printReturnPredictionSection.m` (l. 152) ; `getSignalInfo.m` (l. 1-12) ; `sendUserResults.m` (l. 1-8) ; `Functions/Asset pricing/estFactorRegs.m`, `runUnivSort.m`, `calcPtfRets.m` (par recherche de `pret`, `lag`, `longShort`) ; `Library Update/Functions/getFFFactors.m` (l. 120-137).

**Clone AI-Powered-Scholarship** : `Functions & Scripts/run_protocol.m` (l. 1-75, en entier) ; `README.md` (l. 1185-1222, 1404-1409, et recherche de `v0.4`, `toolkit`).

**Recherche de termes** : sur tout le texte suivi du clone AA (`git grep -I -i -F`), puis hors du code de tiers (`Functions/Utilities/jplv7`, `Functions/Utilities/export_fig`, `Library Update/Resources`).

**Non lus** : voir section 7. Aucun programme du clone n'a été lancé ; aucune donnée (WRDS, Chen et Zimmermann) n'est sur disque ; tout ce qui suit est lecture du code, non exécution.

## 2. Recherche de termes

Compte de lignes trouvées, sur tout le clone puis hors code de tiers.

| terme | tout | hors tiers | ce que c'est |
|---|---|---|---|
| e-value | 15 | 15 | faux positif : en-têtes d'arguments nom-valeur (`Name-Value`) |
| e-process, anytime, martingale, optional stopping | 0 | 0 | rien |
| sequential | 14 | 1 | tiers (jplv7, export_fig) ; hors tiers, un commentaire du code SAS de Gibbs (tirage séquentiel) : sans rapport |
| likelihood ratio | 11 | 0 | tiers seulement (jplv7 : cointégration, VAR) ; aucun appel depuis le protocole (`ols_gcbma`, `lrratio`, `johansen` : 0 appel hors jplv7) |
| Bayes factor, model averaging | 2, 7 | 0, 0 | tiers seulement (jplv7 `ols_gcbma.m`, moyenne bayésienne de modèles) ; jamais appelé par le protocole |
| stacking | 14 | 0 | tiers (empilement de vecteurs) : sans rapport |
| encompass | 0 | 0 | rien |
| spanning | 20 | 20 | **le test d'enjambement du protocole** (section 3, (ii)) |
| benchmark | 10 | 9 | fonctions d'étalonnage du signal contre chaque anomalie (`makeAnomBenchmarkResults.m`, `checkFillAnomalies.m`, `runTestSignal.m`) |
| baseline | 1 | 1 | faux positif (`\baselineskip`, mise en page) |
| null | 33 | 5 | faux positifs (`data _null_` en SAS ; tiers) ; aucun nul statistique nommé |
| multiple testing, false discovery, Bonferroni, Holm | 0 | 0 | rien |
| FDR | 4 | 4 | faux positif (`coeffDraw` dans le code SAS de Gibbs) |
| pre-regist, preregist, pre-commit, seal | 0 | 0 | rien |
| hash | 2 | 0 | tiers (`export_fig.m`) : sans rapport |
| zoo (ajouté) | 12 | 9 | sections 4 et 6 du rapport imprimé : signal contre le zoo d'anomalies ([E42], [E46]) |
| out-of-sample, haircut (ajoutés) | 0 | 0 | rien |
| language model, LLM, GPT, openai (ajoutés) | — | — | aucun ; les seules lignes trouvées sont des faux positifs (`FillMonths`) |

## 3. Lecture par composante

### P — juger une proposition contre ce qui est déjà connu : **pris (hors modèle de langue, 2023)**

La boîte à outils est un protocole pour tout signal nouveau proposé : « This script can also be used to perform all recommended tests in the protocol for testing new anomalies proposed in Novy-Marx and Velikov (2023) by just changing the test signal input. » [E02], et « This repository contains a beta version of the MATLAB Toolkit that accompanies Novy-Marx and Velikov (2023) » [E01]. Le rapport imprimé pose la question contre le connu en toutes lettres : « 'With so many anomalies, it is possible that any proposed, new cross-sectional ', ... 'predictor is just capturing some combination of known predictors. It is consequently ', ... 'natural to investigate to what extent the proposed predictor adds additional ', ... 'predictive power beyond the most closely related anomalies. ' » [E32]. Le plan du rapport a deux étapes contre le connu : « % 5. Does it survive the most closely related anoms? » [E45] et « % 6. Does it add anything to the whole zoo? » [E46]. L'archive est celle de Chen et Zimmermann : « [anoms, labelsCZ, anomaly_summary] = getChenZimmermanAnomalies(); » [E03], qui « loads the anomaly signals from the % Chen and Zimmerman (2022) open-source asset pricing library » [E04], version de mars 2022 (« % These are the file IDs from the March, 2022 release. » [E05]), plus trois anomalies ajoutées à la main (« % WRDS doesn't let CZ share these three anomalies, so we need to add them » [E06]). Licence : « MIT License Copyright (c) 2023 Mihail Velikov » [E47] ; commit de l'étiquette daté du 25 janvier 2023 (`git log`). Le proposeur est une personne (section (i)). **Le principe est donc pris, hors modèle de langue, au plus tard en janvier 2023** — antérieur à NMV 2025, qui l'applique.

### (i) — proposeurs modèles de langue : **non trouvé**

Le signal vient d'un fichier soumis par une personne : formulaire de l'application en ligne (`getSignalInfo.m` l. 1-3) ou saisie à la main (`test_signal.m` l. 26-32) ; les résultats sont renvoyés par courriel, « % Send the user an email with the zipped output sendUserResults(signalInfo) » [E12]. Aucune mention de modèle de langue dans le clone (section 2). Le modèle de langue n'apparaît que dans NMV 2025, qui appelle cette boîte à outils sur des signaux minés.

### (ii) — nul formé d'une mise en commun ajustée des lois de l'archive : **pris sous forme fréquentiste, en échantillon (régression d'enjambement)** ; **voisin proche** pour la mise en commun du zoo entier

**(a) Le test *Close Span*.** La fonction dit ce qu'elle fait : « It finds the most-closely related anomalies and runs Fama-MacBeth % regressions and spanning tests controlling for them. » [E18]. Le rendement expliqué est celui du signal testé, long-court en quintiles pondérés par la capitalisation aux bornes du NYSE (`resBasicSorts(1,1)` : « % NYSE breaks ind = makeUnivSortInd(testSignal, 5, NYSE); % Value-weighted sort resBasicSorts(1, count).res = runUnivSort(ret, ind, dates, me, 'tcosts', tcosts, ... » [E16], premier des modèles « for f = [1 3 4 5 6] » [E17] ; dernière colonne = long-court, « longShortPtf = pret(:,end) - pret(:,1); » [E15]). Chaque anomalie de l'archive est convertie en stratégie de la même façon : « % Run a quintile, value-weighted NYSE breakpoints sort ind = makeUnivSortInd(anomSignal, 5, NYSE); ind = 1*(ind==1) + 2*(ind==5); » [E14]. La régression jointe régresse le rendement du signal sur une constante, les six anomalies proches et six facteurs : « X = [ones(size(y)) spanX ff6(s:e, 2:end)]; resCloseSpan(nCloseAnoms+1, 1) = nanols(y, X); » [E24], les six facteurs étant « ff5 = [const mkt smb2 hml rmw cma]; ff6 = [ff5 umd]; » [E25] (la colonne 1, constante, est retirée par `2:end`). Les six régressions une à une : « X = [ones(size(y)) resAnoms(I(i)).pret(s:e,end) ff6(s:e, 2:end)]; resCloseSpan(i, 1) = nanols(y, X); » [E23]. L'appel du protocole est « [resCloseFMB, resCloseSpan, closeLabels] = makeCloseAnomResults(resCorrels, resAnoms, anoms, labels, testSignal, resBasicSorts, timePeriod); » [E11]. Le rapport trace aussi, pour chaque anomalie de l'archive, le t de l'alpha d'un enjambement univarié sans facteurs, sur tout l'échantillon : « res = (nanols(resBasicSorts(1,1).res.pret(:,end), ... [ones(size(resBasicSorts(1,1).res.pret(:,end))) ... resAnoms(i).pret(:,end)])); a(count,4) = res.tstat(1); » [E48] (histogramme, sans seuil). Le rapport le dit de même : « 'that regress returns to the ', signalChar, ' strategy onto the returns of ', ... 'the ', nCloseAnomsChar, ' most closely-related anomalies and ', ... 'the six Fama-French factors. » [E33].

**Statistique** : moindres carrés ordinaires, `nanols` appelant « res = ols(y,x); » [E26], erreurs classiques sous homoscédasticité et indépendance : « results.sige = sigu/(nobs-nvar); tmp = (results.sige)*(diag(xpxi)); » [E27], « results.tstat = results.beta./(sqrt(tmp)); » [E28]. La statistique retenue est celle de la constante (l'alpha), ligne 1 du tableau : « a(:,end) = resCloseSpan(nCloseAnoms+1).beta'; tA(:,end) = resCloseSpan(nCloseAnoms+1).tstat'; » [E35], reprise dans le résumé du rapport : « alphaClose = sprintf('%2.0f', 100*Results.Tab_CloseSpan.a(1,end)); tstatClose = sprintf('%2.2f', Results.Tab_CloseSpan.tA(1,end)); » [E34].

**Seuil** : **aucun dans la boîte à outils** pour ce test ; la statistique est imprimée, non jugée. Le seul 1,96 du code MATLAB hors tiers compte des alphas de tris de robustesse dans le texte imprimé : « numAlphasSig = num2words(sum(sum(Results.Tab_RobustSort.PanelB.tA(:,2:end)>=1.96))); » [E44]. Le seuil 1,96 sur ce test est celui de NMV 2025 (question 3).

**Choix des six anomalies proches.** Pour chaque anomalie : R² ajusté de la régression du rendement du signal sur celui de l'anomalie, et corrélation des signaux en coupe : « y = resBasicSorts(1,1).res.pret(s:e,end); X = [ones(size(y)) resAnoms(i).pret(s:e,end)]; res = nanols(y, X); spanR2(i,1) = res.rbar; » [E19], « anomCorr(i,1) = resCorrels(i,2); » [E20] ; somme des rangs et tri décroissant, « combinedRank = tiedrank(spanR2) + tiedrank(abs(anomCorr)); % Sort based on the combined rank [~, I] = sort(combinedRank, 'descend'); » [E21] ; nombre fixé, « nCloseAnoms = 6; » [E22]. La corrélation est celle de rangs (Spearman) : la fonction rend deux sorties, « function [rhoS,rhoP]=calcPanelCorrels(var1,var2) » [E29], affectée à une ligne de deux colonnes par « resCorrels(i, :) = calcPanelCorrels(anoms(s:e, :, i), testSignal(s:e, :)); » [E30] — selon la sémantique de MATLAB (non exécuté), seule la première sortie est prise ; le texte imprimé confirme : « ' most-closely related anomalies are picked as those with the highest combined rank ', ... 'where the ranks are based on the absolute value of the Spearman correlations in Panel B ', ... » [E31]. Une anomalie n'entre que si elle couvre plus de dix ans de la période du signal et plus de 40 % des capitalisations en moyenne : « N = 120; mcapThresh = 0.40; » [E07], « if e > s+N » [E08], « keepAnoms(i,1) = (meanPrctOfMktCapObs > mcapThresh); » [E09]. Le nombre d'anomalies de l'archive n'est pas dans le code (il dépend du fichier téléchargé) : non lu.

**Ajustement sur les données** : oui, et sur **le même échantillon** que le test. Le choix des six utilise le rendement du signal sur la période même du test (R² de [E19]) ; les coefficients de la combinaison sont ajustés par moindres carrés sur cette période ; la statistique de l'alpha ne tient compte ni du choix des six parmi l'archive, ni de l'ajustement préalable. Il n'y a pas de mise en commun de **lois prédictives** (densités) : ce sont des **séries de rendements de portefeuilles** combinées linéairement.

**Verdict (ii-a), dit fort** : le nul selon lequel le rendement du signal nouveau est expliqué par une combinaison linéaire, ajustée sur les données, des stratégies connues de l'archive (les six plus proches) et des facteurs, est **pris sous forme fréquentiste**, avec une statistique de Student de l'alpha, dès la boîte à outils de 2023. C'est la forme exacte du crible de NMV 2025 (question 3). Ce qui sépare encore notre (ii), dans le code lu : lois prédictives mises en commun et non rendements de portefeuilles ; archive entière et croissante (survivantes promues par l'organisme) et non six anomalies choisies dans une archive fixe ; ajustement avant le gel et non sur l'échantillon du test. Aucune de ces différences n'est démontrée décisive ici.

**(b) La mise en commun du zoo entier (section 6 du rapport).** Six méthodes combinent toutes les anomalies retenues en une prévision de rendement, sans puis avec le signal, par exemple « combStrats(count,1).eret = makeAverageRank(filledAnoms, me); combStrats(count,1).eret_enh = makeAverageRank(cat(3, filledAnoms, filledSignal), me); » [E36] ; les méthodes estimées le font (texte du bloc Fama et MacBeth ; même phrase pour les moindres carrés partiels et IPCA, `makeCombStrats.m` l. 134-136 et 155-157, phrase voisine pour LASSO, l. 174-180) « using only data in the investor''s ', ... 'information set at the time of portfolio formation. The estimation uses rolling ', ... 'ten years of data, so the actual strategies begin ten years later for this combination method. » [E37] ; pour Fama et MacBeth, fenêtre « T = 120; » [E38] et coefficients moyens glissants « if i >= T bMean = mean(betas(i-T+1:i, :), 1, 'omitnan'); » [E39] ; le signal d'un mois sert au rendement du mois suivant (« % Lag market cap and the portfolio index lmcap = lag(mcap,1,nan); lind = lag(ind,1,0); » [E40]). C'est une **prévision mise en commun et ajustée de toute l'archive, en pseudo hors échantillon** — la plus proche, dans la forme, de notre nul d'archive ajusté. Mais la comparaison n'est **qu'un graphique** : déciles long-court sans et avec le signal, « yWithout(:, i) = res1.pret(:,end); yWith(:, i) = res2.pret(:,end); » [E41], et une phrase de croissance d'un dollar, « '\\$1 investment in the ', nAnoms, '-anomaly combination strategy ', ... 'grows to \\$', endDollarWithout, ', while \\$1 investment in the combination ', ... 'strategy that includes ', signalChar, ' grows to \\$', endDollarWith, » [E43], sous le titre « ' add relative to the whole zoo?} » [E42]. Aucune statistique, aucun seuil, aucune règle. Statut : **voisin proche** (nul de forme proche, sans test).

### (iii) — e-processus ou validité à tout instant d'arrêt : **non trouvé**

Statistiques de Student à échantillon fixé, erreurs classiques ([E27], [E28]) ; aucun seuil appliqué par la boîte à outils au test d'enjambement ; aucune correction de multiplicité (choix des six, deux étapes, plusieurs tris) ; aucun des termes e-value (au sens statistique), e-process, anytime, martingale, optional stopping, Bonferroni, Holm, false discovery (section 2). Le code de tiers contient une moyenne bayésienne de modèles et des rapports de vraisemblance, jamais appelés par le protocole.

### (iv-a) — prédictions engagées avant que les données existent : **non trouvé**

Le signal est soumis comme fichier de données déjà construit ; la période du test est celle où le signal existe (`runTestSignal.m` l. 59-63) ; tout l'échantillon disponible sert, à la fois au choix des six proches et au test. Aucun engagement, scellement ni horodatage (section 2). L'estimation glissante des combinaisons ([E37]-[E40]) est un pseudo hors échantillon d'estimation, pas un engagement du proposeur : je ne la compte pas comme (iv-a).

### (iv-b) — statistique calculée hors des agents : **voisin**

La statistique est calculée par un programme fixe à partir d'un fichier soumis, et renvoyée par courriel ([E12]) ; le proposeur est une personne, non un agent ; rien n'isole le calcul du proposeur (le code est ouvert et le README invite à changer l'entrée, [E02]), donc rien n'empêche d'essayer jusqu'à passer.

## 4. Réponses aux questions

1. **Que calcule *Close Span* ?** Une régression par moindres carrés ordinaires du rendement mensuel brut de la stratégie long-court du signal (quintiles, pondération par la capitalisation, bornes du NYSE) sur une constante, les rendements long-court des anomalies proches (une à la fois, puis les six ensemble) et les six facteurs (marché, taille, valeur, rentabilité, investissement, momentum) ([E16], [E23]-[E25]). Statistique : t de Student de la constante (alpha), erreurs classiques ([E26]-[E28], [E34], [E35]). Seuil : aucun dans la boîte à outils ; 1,96 en valeur absolue chez NMV 2025 ([P04]).
2. **Choix des proches** : six ([E22]), par la somme des rangs du R² ajusté de la régression univariée du rendement du signal sur celui de chaque anomalie et de la valeur absolue de la corrélation de Spearman des signaux ([E19]-[E21], [E29]-[E31]) ; archive : le zoo de Chen et Zimmermann, version de mars 2022, plus trois anomalies ([E03]-[E06]), filtrée par dix ans et 40 % de couverture ([E07]-[E09]). L'ensemble est **choisi sur les données du test et combiné par une régression ajustée sur ces mêmes données** : c'est une mise en commun linéaire ajustée, en échantillon, de **rendements** de six stratégies de l'archive, non de lois prédictives de l'archive entière. La mise en commun du zoo entier existe ailleurs dans le protocole ([E36]-[E43]), ajustée en glissant, mais sans test.
3. **Indice 7 de `resCloseSpan`** : dans v0.4.0, `resCloseSpan(nCloseAnoms+1)` avec six proches, soit la **régression jointe** sur les six proches et les six facteurs ([E22], [E24]) ; `tstat(1)` est le t de l'alpha. NMV 2025 lit exactement cette valeur, « finalRes.CloseSpanT(i) = ResStruct.resCloseSpan(7).tstat(1); » [P03], et sélectionne par « temp = finalRes(abs(finalRes.CloseSpanT)>1.96,{'numer','denom','signal','varName'}); » [P04]. **Réserve** : NMV 2025 dit utiliser une préversion, « **Important**: The results in Novy-Marx and Velikov (2025) use the pre-release v0.4 of the MATLAB Toolkit. » [P05], et ses appels ne correspondent pas aux signatures de v0.4.0 : « [anoms, resAnoms] = makeAnomStratResults(anoms, ret, dates, me, tcosts, NYSE); » [P01] et « runTestSignal(signalInfo(i), anoms, labels, resAnoms); » [P02], contre « function [resAnoms] = makeAnomStratResults(anoms) » [E13] et « function runTestSignal(signalInfo, anoms, labels) » [E10]. Le code effectivement lancé en 2025 n'est donc pas, fichier pour fichier, l'étiquette v0.4.0 : que l'indice 7 y soit la régression jointe (six proches, six facteurs) est établi pour v0.4.0 seulement, probable pour la préversion, non établi.
4. **Multiplicité, validité à tout instant d'arrêt, engagement avant les données** : absents tous trois du code lu (section 3, (iii) et (iv-a) ; section 2).
5. **Le nul de NMV est-il pris pour (ii) sous forme fréquentiste ? Oui, dans cette forme.** Le crible de NMV 2025 est un test d'enjambement : la proposition est jugée contre une combinaison linéaire ajustée des six stratégies connues les plus proches de l'archive de Chen et Zimmermann et des six facteurs, par le t de l'alpha à 1,96. Le statut de NMV pour (ii) dans la note v3 (voisin proche, forme inférée) doit monter à **pris sous forme fréquentiste, en échantillon**, forme lue sur v0.4.0 (réserve de version, question 3) ; ce nul est publié depuis 2023, antérieur à NMV 2025. Ce qui reste à notre (ii) : lois prédictives et non rendements ; archive entière croissante ; ajustement avant le gel. Nœud 1.

## 5. Table de la pièce

| composante | AA (boîte à outils v0.4.0, code seul) | preuve |
|---|---|---|
| **P** | **pris, hors modèle de langue (2023)** | [E01], [E02], [E32], [E45], [E46], [E47] |
| **(i)** | non trouvé | formulaire et saisie à la main, [E12] ; aucun terme (section 2) |
| **(ii)** | **pris sous forme fréquentiste, en échantillon** (régression d'enjambement contre six anomalies proches choisies sur les données et six facteurs, t de l'alpha) ; **voisin proche** pour le zoo entier mis en commun en glissant, sans test | [E14]-[E31], [E33]-[E43] |
| **(iii)** | non trouvé | [E27], [E28], [E44] ; section 2 |
| **(iv-a)** | non trouvé | `runTestSignal.m` l. 59-63 ; [E19] |
| **(iv-b)** | voisin | [E02], [E12] |
| **conjonction** | non trouvée | (i), (iii), (iv-a) absents |

## 6. Nœuds pour Lazar

Rien n'est déclaré libre ; le verdict en vigueur sur O4 reste **occupée en partie**. Les options prudentes (R4) sont indiquées, non conclues.

1. **(ii) sous forme fréquentiste.** Porter dans la note d'englobement et dans la table des pièces de priorité haute : (ii) **pris sous forme fréquentiste, en échantillon**, par AA (2023) et appliqué mécaniquement par NMV 2025 (au lieu de *voisin proche, forme inférée*). Option prudente : l'écrire ainsi, et ne revendiquer de (ii) que ce qui reste (lois prédictives mises en commun, archive entière croissante, ajustement avant le gel), chacune de ces différences étant à défendre comme non triviale.
2. **Mise en commun du zoo entier.** Ajouter AA comme voisin proche de (ii) pour sa combinaison glissante de toute l'archive, sans puis avec le signal, comparée sans test ([E36]-[E43]) ; c'est, dans la forme, la base d'archive mise en commun et ajustée que notre juge prend pour nul. Option prudente : la citer à côté de SEADS dans les citations obligatoires de O4.
3. **Citation.** AA est cité Novy-Marx et Velikov (2023) par son README ([E01]) et 2024 par NMV 2025 (note v3) ; l'article n'est pas lu. Option prudente : citer l'article et la boîte à outils v0.4.0 au commit `f08a77f7…`, toute affirmation étant dite *lue sur le code* tant que le PDF n'est pas fourni.
4. **Version du code de NMV 2025.** L'indice 7 est établi pour v0.4.0, non pour la préversion qu'utilise NMV 2025 ([P01], [P02], [P05]). Décider s'il faut demander la préversion aux auteurs (contact extérieur : je rédige, Lazar envoie) ou dire la réserve.
5. **Article SSRN 4338007.** Fournir le PDF (ou une version publiée) : l'article peut contenir une règle de décision, un seuil, une correction de multiplicité ou une discussion du hors échantillon absentes du code.

## 7. Ce qui reste non lu

- **L'article** *Assaying Anomalies* (SSRN 4338007), refusé ; le site `assayinganomalies.com` et ses tutoriels ; la préversion v0.4 utilisée par NMV 2025.
- **Code non lu** : `makeDendrogramResults.m`, `makeAverageRank.m`, `makeWeightedAverageRank.m`, `makePLSRes.m`, `makeIPCARes.m`, `runIPCAforMonth.m`, `num_IPCA_estimate_ALS.m`, `makeLassoRes.m`, `fillVar.m`, `plotNameHistogram.m`, `setAssayPath.m` ; `Functions/Asset pricing/` hors des recherches dites (dont `runFamaMacBeth.m`, `makeUnivSortInd.m`, `getAnomalySignals.m`, `calcGenAlpha`) ; `makeResToPrint.m` hors des plages dites ; les fonctions d'impression `prt/` hors des plages dites ; `use_library.m`, `setup_library.m`, `Library Update/` hors de `getFFFactors.m` ; tout le code de tiers (jplv7, export_fig) hors de `ols.m`. Les PDF du dossier `Utilities` et les ressources de WRDS ne sont pas ouverts (consigne).
- **Références de la pièce qui pourraient toucher la conjonction** (nommées dans le code, non lues) : Chen et Zimmermann (2022), l'archive ([E04]) ; Chen et Velikov (2022), méthodes de combinaison du zoo (`printCombStratsSection.m` l. 55 ; `makeCombStrats.m` l. 177) ; Jensen et al. (2021), nommés pour le dendrogramme (`runTestSignal.m` l. 85) — à vérifier sur pièce s'il s'agit de l'étude bayésienne du zoo, qui toucherait (ii) sous forme bayésienne ; Haugen et Baker (1996), Lewellen (2015), Light, Maslov et Rytchkov (2017), Kelly, Pruitt et Su (2019) (`makeCombStrats.m` l. 113-155), prévisions mises en commun ; Novy-Marx et Velikov (2016), alphas généralisés (`makeBasicSortsResults.m` l. 114).

## 8. Incidents

- Aucun refus de permission, de crochet ni de classifieur.
- Article SSRN refusé avant cette lecture (pièce versée, non tentée de nouveau) ; aucun accès réseau ici.
- La recherche du sigle LLM, insensible à la casse, renvoie des faux positifs (`FillMonths`) ; signalé, sans effet.
- Le clone AA est superficiel (un commit) : l'historique avant v0.4.0 n'est pas lisible ici.
