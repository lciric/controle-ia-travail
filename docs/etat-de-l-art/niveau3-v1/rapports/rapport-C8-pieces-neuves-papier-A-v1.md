# Rapport C8 — pièces neuves signalées par le moteur de recherche, lues contre H1, H2, le lemme, le théorème négatif, H6, la transposition jeton → action et H8 (papier A) — v1

Date : 2026-11-10, vers 11:11 UTC (heure relevée par `date -u`). Rédacteur : sous-agent neuf, lecteur du lot C8 de l'état de l'art de niveau 3. Il n'a écrit aucune pièce du programme.
Consigne suivie : `docs/etat-de-l-art/niveau3-v1/consignes/consigne-commune-lecteurs-v1.md`, lue en entier. Rapports antérieurs situés : C1, C2, C5 (sections de verdict et tableaux par composante).

## 0. Verdict en tête

**Pas de collision. Aucune zone revendiquée n'est occupée en entier par les neuf pièces lues.**

- **H2.** Les quatre pièces « somme cumulée » lisent toutes des signaux **externes** (statistiques du texte, probabilités de sortie, télémétrie, captures d'écran). Aucune ne lit une sonde sur les activations de l'agent. Aucune ne traite un sabotage voulu par l'agent. La plus proche est **CURA (2608.27808)** : somme cumulée de Page sur la trajectoire d'un agent, **garantie de fausse alarme certifiée, calibrée sur les seules trajectoires réussies, sans exemple d'échec**, et variante valable à tout instant par l'inégalité de Ville. C'est le « squelette séquentiel boîte noire » que N-007 dit déjà exister ; il gagne un second titulaire, à citer à côté d'E-valuator.
- **Lemme.** Les deux sources classiques sont maintenant lues sur PDF. Howard et collègues portent la borne de mélange normal (propositions 5 et 6, p. 28 ; lemme 2, p. 9) ; ils la disent eux-mêmes connue (Robbins, 1970). Arias-Castro, Candès et Plan portent la dichotomie somme contre maximum (p. 2-3, 6-7 ; théorème 1, p. 13 ; théorème 5, p. 17-18). **Aucune des deux n'écrit la phrase « la puissance ne dépend que du budget total, pas de sa répartition ».** Mais le fait est porté, sous sa forme quadratique et à horizon fixe, par Arias-Castro et collègues (p. 2, p. 6-7) : voir 2.8. L'invariance L1 reste donc élémentaire et de parenté classique, comme C2 l'avait écrit.
- **H8.** Deux pièces occupent le **socle non revendiqué** (ce que la sonde mesure vraiment décide de sa lecture hors du contexte d'ajustement) : 2609.10739 (p. 1, 4) et 2607.13346 (p. 1, 4, 7). **La pièce revendiquée, la prédiction de la robustesse adverse par le construit, n'est dans aucune des deux.**
- **H6, transposition jeton → action, théorème négatif.** Rien dans ce lot. Libres dans les pièces lues (R8 : « non trouvé ici », rien de plus).
- **Écart de titre à signaler.** Le fichier `2607.13346v2.pdf` ne s'intitule pas « The Refusal Residue » : son titre, page 1, est « PRISM: Stress-Testing Alignment-Faking Claims » (version 2 du 5 novembre 2026). Le titre signalé par le moteur de recherche n'apparaît nulle part dans le texte extrait.

Verdict par pièce, en une ligne :

| Pièce | Énoncé touché | Verdict |
|---|---|---|
| 2606.12476v3, Itkin, « Quickest Detection of Hallucination Onset » | H2 ; lemme (de loin) | **voisine** ; signal externe ; aucune garantie ; contre-résultat sur la part de l'accumulation |
| 2608.02464v1, Dubey, « Real-Time Detection and Repair of LLM Agent Failures » | H2 | **occupe en partie, en boîte noire** : composantes (3) et, en partie, (6) ; p. 4, 5 |
| 2608.27808v1, Kumar et collègues, « CURA » | H2 | **occupe en partie, en boîte noire** : composantes (3) et (4), calibrage sans exemple d'échec ; p. 1, 3, 4, 16 |
| 2607.20129v2, Ettifouri et collègues, contrôleur « MGT-B » | H2 | **voisine** (lointaine) ; garantie expressément non revendiquée |
| 2606.08106v1, Shawn, « PACE » | H2 | **voisine** par la méthode seule ; autre objet (accepter une modification de l'agent) |
| 2609.10739v2, Jayabahu, « The Truth Was Never Gone » | H8, H1 | **occupe en partie** le socle non revendiqué de H8 ; contre-résultat pour les sondes ajustées sur contextes honnêtes |
| 2607.13346v2, Mehta, « PRISM » (signalée comme « The Refusal Residue ») | H8, H1 | **occupe en partie** le socle non revendiqué de H8 ; contre-résultat pour H1 |
| 1810.08240v9, Howard, Ramdas, McAuliffe, Sekhon | lemme (borne de mélange) | **source classique, portée sur PDF** ; ne contient pas l'invariance au budget |
| 1007.1434v2, Arias-Castro, Candès, Plan | lemme (L1, L2) | **source classique, portée sur PDF** ; porte la dichotomie ; porte l'invariance au budget sous forme quadratique, sans l'écrire comme telle |

## 1. Méthode, pièces, limites de ma lecture

Lecture par `pdftotext`, page par page, en deux modes (avec mise en page ; en ordre de lecture pour les papiers à deux colonnes). Empreintes recalculées par `sha256sum` avant lecture.

| Pièce | Chemin de dépôt | Empreinte (début) | Pages |
|---|---|---|---|
| 2606.12476v3 | `docs/sources/pdf/niveau3-v1/lot7/2606.12476v3.pdf` | `0412750524774889` | 18 |
| 2608.02464v1 | `docs/sources/pdf/niveau3-v1/lot7/2608.02464v1.pdf` | `788c825fc0cad65c` | 16 |
| 2608.27808v1 | `docs/sources/pdf/niveau3-v1/lot7/2608.27808v1.pdf` | `3fb73b02cc646e0b` | 25 |
| 2607.20129v2 | `docs/sources/pdf/niveau3-v1/lot7/2607.20129v2.pdf` | `1787e8085745f61c` | 11 |
| 2609.10739v2 | `docs/sources/pdf/niveau3-v1/lot7/2609.10739v2.pdf` | `55bdb17e4c90b078` | 40 |
| 2607.13346v2 | `docs/sources/pdf/niveau3-v1/lot7/2607.13346v2.pdf` | `c29351f1db3dcc28` | 10 |
| 1810.08240v9 | `docs/sources/pdf/niveau3-v1/lot7/1810.08240v9.pdf` | `eb3efd547349adfb` | 48 |
| 1007.1434v2 | `docs/sources/pdf/niveau3-v1/lot7/1007.1434v2.pdf` | `40cc6f96f6f12cd3` | 26 |
| 2606.08106v1 | `docs/sources/pdf/2606.08106v1.pdf` | `779f49607688fd06` | 12 |

Les huit premières sont sur la branche `prep/etat-de-l-art-niveau3-pieces-v1` (commit `2eb9a1ca`, selon la consigne du lot). Je n'ai pas ouvert cette branche (interdit 1) : je les ai lues dans le dossier temporaire donné par la consigne, `…/scratchpad/lotC8/pdf/`. Je n'ai donc **pas** comparé mes empreintes aux fichiers compagnons `.sha256` de cette branche ; les débuts d'empreinte ci-dessus sont ceux que j'ai calculés sur les fichiers lus. Pour 2606.08106, l'empreinte calculée concorde avec le fichier compagnon du dépôt.

**Réserve franche sur « lire en entier ».** Je ne l'ai pas tenu partout.

- 2606.12476 : lues, pages 1 à 5, 9, 11, 12 ; en partie, 7 et 18. Le reste (preuves, annexes) par mots.
- 2608.02464 : lues, pages 1 à 5 ; en partie, 10, 12, 13. Le reste par mots.
- 2608.27808 : lues, pages 1 à 4 ; en partie, 5, 7, 16, 17. Annexes 8 à 25 par mots.
- 2607.20129 : lues, pages 1 à 4. Pages 5 à 11 (expériences, références) non lues ligne à ligne.
- 2606.08106 : lues, pages 1 à 5. Pages 6 à 12 non lues ligne à ligne.
- 2609.10739 : lues, pages 1 à 4, 8, 9 ; en partie, 6. Pages 5, 7 et annexes 10 à 40 par mots.
- 2607.13346 : lues, pages 1 à 7 (tout le corps ; le résumé de la page 1 sort en deux colonnes entrelacées). Pages 8 à 10 (références, annexes) survolées.
- 1810.08240 : lues, les passages demandés seulement : pages 1, 5, 9, 10, 12, 13, 19, 28. Le reste par mots (« power », « alternative », « budget », « allocation »).
- 1007.1434 : lues, pages 1 à 13 ; en partie, 16 à 18. Pages 19 à 26 non lues.

Mots cherchés partout : « activation », « hidden », « probe », « internal », « anytime », « martingale », « e-process », « Ville », « guarantee », « adversar », « sabotage », « horizon », « agent ». Un passage sans aucun de ces mots a pu m'échapper dans les pages non lues ligne à ligne.

**Contrôle des citations.** Script `/tmp/claude-0/-home-user-controle-ia-travail/a26149b8-c735-5fa7-914e-afb00d165aed/scratchpad/lotC8/verifier_citations.py` (hors dépôt). Il relit ce rapport, en tire chaque citation, et la cherche dans le texte de la page citée, dans les deux modes d'extraction, après retrait des espaces, des traits d'union et des césures, et mise à plat des guillemets. Essayé d'abord sur un cas juste, un cas altéré et une mauvaise page (R5). Compte en section 7.

Format : **[Qnn]** fichier, page, citation exacte entre guillemets français. Les chiffres cités sont « imprimés par les auteurs ». Les exposants et indices sont aplatis par l'extraction (par exemple « p1/4 » pour p à la puissance un quart).

## 2. Pièce par pièce

### 2.1 2606.12476v3 — « Quickest Detection of Hallucination Onset: Delay Bounds and Learned CUSUM Statistics »

Igor Itkin, chercheur indépendant ; 4 juillet 2026 (page 1).

**Ce qu'elle fait.** Elle pose le début d'une hallucination, dans un texte en cours de génération, comme une détection de rupture au plus vite. Elle lit un réseau récurrent causal comme une somme cumulée de Page à incrément appris, et mesure son retard contre la borne de Lorden.

- **[Q01]** `2606.12476v3.pdf` p. 1 : « We formulate hallucination onset detection as a quickest change detection problem. »

**Le signal est-il interne ? Non.** Il est fait de statistiques du texte, de signaux d'inférence textuelle et des probabilités de sortie du générateur. L'auteur oppose lui-même son détecteur aux sondes boîte blanche.

- **[Q02]** `2606.12476v3.pdf` p. 3 : « the feature vector extracted for token t (text statistics, NLI signals, generator log-probabilities) »
- **[Q03]** `2606.12476v3.pdf` p. 12 : « Because the detector needs no access to the generating model, it remains applicable to closed-source APIs where white-box probes do not »
- **[Q04]** `2606.12476v3.pdf` p. 11 : « internal-state probes among them, at the cost of black-box applicability »

**Garantie ? Non.** La fausse alarme est une longueur moyenne avant fausse alarme, mesurée sur le flux des jetons fidèles, par balayage du seuil. Ce n'est pas une garantie valable à tout instant sur un épisode. La borne citée est la borne classique de Lorden, atteinte par la somme de Page.

- **[Q05]** `2606.12476v3.pdf` p. 4 : « Reporting against ARL0 keeps the empirical operating point in the same units as the bound »
- **[Q06]** `2606.12476v3.pdf` p. 5 : « and the CUSUM rule of Page [13] attains this floor asymptotically [10] »

**Énoncés touchés.** H2, par la seule composante (3), à l'échelle du jeton et non de l'action, sur un phénomène non adverse. Le lemme, de loin : la proposition 1 (p. 6 et 18) dit que le retard d'un détecteur à score est fixé par le taux d'information du score ; c'est la théorie classique de la rupture, pas un énoncé à budget borné.

**Verdict : voisine.**

**Contre-résultat à retenir (défavorable à H2).** À fausse alarme égale, l'accumulation n'explique qu'une petite part du gain ; l'essentiel vient de la qualité du score par pas. Et à 1 % de fausse alarme par jeton, tous les détecteurs manquent plus des deux tiers des débuts.

- **[Q07]** `2606.12476v3.pdf` p. 1 : « A controlled decomposition attributes the speed advantage mostly to a better per-token score rather than to temporal accumulation. »
- **[Q08]** `2606.12476v3.pdf` p. 2 : « the sequential accumulation contributes about a quarter of the reduction »
- **[Q09]** `2606.12476v3.pdf` p. 1 : « at this false-alarm budget every detector catches under a third of onsets »

### 2.2 2608.02464v1 — « Real-Time Detection and Repair of LLM Agent Failures »

Sunny Dubey ; 3 août 2026 (page 1).

**Ce qu'elle fait.** Un moniteur à une classe, ajusté sur les seules exécutions saines, lit la télémétrie observable de chaque pas d'un agent (plongement de la sortie, incertitude des jetons, métadonnées d'action) et lève une alarme par somme cumulée de Page. Elle le valide sur 2 823 épisodes, puis ferme la boucle par une réparation.

- **[Q10]** `2608.02464v1.pdf` p. 1 : « We ask how much failure detection is achievable from observable step telemetry alone »
- **[Q11]** `2608.02464v1.pdf` p. 2 : « without model internals, without labels, and without a second LLM in the loop »

**Somme cumulée, seuil réglé sur des épisodes sains entiers.** Le seuil est un quantile du maximum de la statistique sur des épisodes sains de validation : c'est le calibrage « sur épisodes honnêtes entiers » que C2 attribue déjà à E-valuator (2512.03109).

- **[Q12]** `2608.02464v1.pdf` p. 4 : « Slow drift keeps each step locally predictable, so a short-memory statistic never crosses threshold; a one-sided CUSUM [2] integrates small persistent shifts instead »
- **[Q13]** `2608.02464v1.pdf` p. 4 : « θ is read from healthy validation episodes and never from test data »

**Détection croissante avec l'horizon après le début de la panne (composante 6, en boîte noire).**

- **[Q14]** `2608.02464v1.pdf` p. 5 : « detection gap is +0.09 when the post-onset horizon is ≤3 steps, +0.14 at 4–8 and +0.40 at ≥9 »

**Ce qu'elle ne fait pas.** Aucune activation ; aucune garantie formelle (le taux est empirique) ; aucun adversaire : les pannes sont injectées ou spontanées. L'auteur concède l'avantage des activations.

- **[Q15]** `2608.02464v1.pdf` p. 3 : « with the weights in hand, activations beat telemetry »

**Verdict : occupe en partie H2, en boîte noire** — composante (3) (p. 4, [Q12]) ; composante (6) en partie (p. 5, [Q14]) ; l'idée « dérive lente sous le seuil d'un moniteur à mémoire courte » est écrite (p. 4, [Q12]) mais non mesurée contre un moniteur par action à 1 %, et hors de toute menace adverse. Composantes (1), (2), (4), (5) : non.

**Contre-résultats (défavorables au programme).**

- La dérive lente échappe : **[Q16]** `2608.02464v1.pdf` p. 12 : « Slow goal drift evades every per-step-surprise monitor tested; only trajectory self-consistency sees it, weakly. »
- Le seuil ne se transporte pas d'un déploiement à l'autre : **[Q17]** `2608.02464v1.pdf` p. 5 : « the primary monitor sits at chance (AUROC 0.527, healthy FA 0.75) »
- Hors du régime de calibrage, la fausse alarme explose : **[Q18]** `2608.02464v1.pdf` p. 10 : « a temperature-matched null still false-alarms on 36% of healthy episodes »

### 2.3 2608.27808v1 — « CURA: Certified Runtime Alarms for Computer-Use Agents »

Divake Kumar, Sina Tayebati, Devashri Naik, Amanda Sofie Rios, Nilesh Ahuja, Omesh Tickoo, Ranganath Krishnan, Amit Ranjan Trivedi (Université de l'Illinois à Chicago, Intel Labs, Capital One) ; 28 août 2026 (page 1).

**Ce qu'elle fait.** Un moniteur externe lit la télémétrie visible du harnais d'un agent d'usage d'ordinateur (361 tâches OSWorld) et en fait un test séquentiel : somme cumulée de Page, seuil choisi par la procédure « apprendre puis tester » sur des trajectoires réussies, avec une borne de fausse alarme en échantillon fini.

- **[Q19]** `2608.27808v1.pdf` p. 1 : « an external monitor that reads only harness-visible telemetry, with no model internals, extra LLM calls, or prompt changes, and turns the running trajectory into a sequential test with certified false-alarm control »
- **[Q20]** `2608.27808v1.pdf` p. 3 : « constructs an online stopping time »
- **[Q21]** `2608.27808v1.pdf` p. 4 : « Calibration uses only successful trajectories and therefore requires no labeled failures. »

**Variante valable à tout instant.** Une martingale de pari sur des valeurs p conformes, bornée par l'inégalité de Ville, uniformément dans le temps (p. 4 ; annexe G.2, p. 16).

- **[Q22]** `2608.27808v1.pdf` p. 4 : « a betting martingale Mt over conformal p-values »
- **[Q23]** `2608.27808v1.pdf` p. 16 : « uniformly over time, that is, valid under optional stopping at every step »
- **[Q24]** `2608.27808v1.pdf` p. 5 : « The anytime-valid martingale variant also respects its bound empirically (FPR 0.097 at α = 0.10), but fires earlier on fewer failures. »

**Résultat principal.**

- **[Q25]** `2608.27808v1.pdf` p. 1 : « its CUSUM alarm detects 42.3% of failures a median of 31 steps before termination at a realized false-alarm rate of 0.066 »

**Ce qu'elle ne fait pas.** Aucune activation ([Q19]). Aucun adversaire : les auteurs le disent trois fois.

- **[Q26]** `2608.27808v1.pdf` p. 1 : « We find no evidence of strategic deception and do not study adversarial evasion »
- **[Q27]** `2608.27808v1.pdf` p. 7 : « so we make no adversarial robustness claim »
- **[Q28]** `2608.27808v1.pdf` p. 7 : « an agent with an incentive to evade could suppress several cheaply: pace its tokens, avoid pivot phrasing, keep trajectories short »

**Verdict : occupe en partie H2, en boîte noire** — composante (3) (p. 4) ; composante (4) (p. 3, 4, 16 : [Q19], [Q22], [Q23]) ; calibrage sur trajectoires réussies seules, sans exemple d'échec (p. 4, [Q21]). Composantes (1), (2), (5) : non. Composante (6) : non trouvée ; au contraire, le moniteur est dit faible sur les échecs « rapides et silencieux » (p. 7).

**Portée pour N-007.** L'énoncé retenu de H2 ne revendique plus le squelette séquentiel boîte noire. CURA ne le fait donc pas tomber. Mais CURA réunit déjà, sur des trajectoires d'agent, trois des traits que l'énoncé retenu met en avant : accumulation additive, garantie uniforme sur l'horizon, calibrage sans exemple négatif. Ce qui reste non trouvé est la réunion avec (1), (2) et (5). CURA est aussi le candidat naturel de la base (i) du plan de N-007 (« accumulation additive sur scores boîte noire »), à côté d'E-valuator.

**Contre-résultats (défavorables au programme).**

- La garantie ne dit rien de la détection et ne tient que sous la loi calibrée : **[Q29]** `2608.27808v1.pdf` p. 4 : « It does not guarantee failure detection, task correctness, or safety, and requires recalibration under distribution shift. »
- Le seuil ne se transporte pas : **[Q30]** `2608.27808v1.pdf` p. 7 : « realized false-alarm rate triples under the new regime »
- Une base triviale résiste : le nombre total de jetons atteint 0,802 d'aire sous la courbe, et le composite ne la bat pas de façon significative (p. 1 : Δ = +0,026, p = 0,101). Leçon pour les bases de G1 : la longueur de l'épisode est une base à battre.
- La variante valable à tout instant paie sa garantie en rappel ([Q24]). C'est le « prix de la garantie toujours valide » que L3 revendique de chiffrer : CURA en donne un point empirique, en boîte noire, sans le chiffrer comme tel.

### 2.4 2607.20129v2 — « CUSUM-Shaped Inference-Time Monitoring and Targeted Re-Decoding for Quantized Small Language Model Reasoning »

El Hassane Ettifouri, Ayoub Belfatmi, Mahaman Sanoussi Yahaya Alassan, Walid Dahhane (Novelis Research, Paris) ; 2 septembre 2026 (page 1).

**Ce qu'elle fait.** Un contrôleur externe (« MGT-B ») surveille des fenêtres de jetons d'un petit modèle quantifié qui raisonne, accumule des facteurs de pari avec une remise à zéro « en forme de somme cumulée », et, à l'alarme, revient à un état antérieur puis redécode.

- **[Q31]** `2607.20129v2.pdf` p. 1 : « It accumulates mixture betting factors with a CUSUM-shaped reset »
- **[Q32]** `2607.20129v2.pdf` p. 2 : « We study a fixed external controller that observes logits and sampled tokens but never changes model weights. »

**Signal.** Les logits de sortie et les jetons tirés : entropie, répétition, changement local. Pas d'activations internes, pas de sonde.

**Garantie.** Expressément non revendiquée.

- **[Q33]** `2607.20129v2.pdf` p. 2 : « its threshold is an empirical operating point, not a theoretical false-alarm certificate »
- **[Q34]** `2607.20129v2.pdf` p. 3 : « does not satisfy a proved e-process condition »

**Énoncés touchés.** H2, par la composante (3) seule, à l'échelle du jeton, sur une dégénérescence de raisonnement, sans agent ni adversaire. Lemme : rien.

**Verdict : voisine (lointaine).** Utile comme rappel de méthode : les auteurs refusent le mot « processus e » parce que leurs fenêtres se chevauchent et ne sont pas échangeables (p. 2, p. 4). Le même scrupule vaut pour des scores de sondes corrélés d'un pas à l'autre ; N-007 l'a déjà pris en compte (calibrage sur épisodes entiers).

- Contre-résultat de portée limitée : le gain ne se transporte pas. **[Q35]** `2607.20129v2.pdf` p. 1 : « the effect does not transfer to Omni-MATH »

### 2.5 2606.08106v1 — « PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents »

ZayxShawn, chercheur indépendant ; 6 juin 2026 (page 1).

**Ce qu'elle fait.** Un agent qui se modifie lui-même ne garde une modification que si un processus e de pari, sur des paires discordantes entre le candidat et le titulaire, franchit 1/α. La garantie est valable à tout instant, par candidat.

- **[Q36]** `2606.08106v1.pdf` p. 1 : « committed only when a testing-by-betting e-process accumulates decisive evidence »
- **[Q37]** `2606.08106v1.pdf` p. 5 : « the probability of ever committing a non-improving candidate is at most α »
- **[Q38]** `2606.08106v1.pdf` p. 2 : « the contribution is this abstraction, locating an anytime-valid test at the commit step, not the test itself (which is standard) »

**Signal.** Des réussites binaires appariées. Rien d'interne.

- **[Q39]** `2606.08106v1.pdf` p. 2 : « consuming only those paired outcomes rather than the proposer’s internals »

**Énoncés touchés.** H2, par la méthode seule (composantes 3 et 4), sur un autre objet : ce n'est pas de la surveillance, il n'y a ni trajectoire d'actions, ni sabotage, ni score de sonde. Le rapport C4 l'a déjà lue pour l'organisme d'idéation.

**Verdict : voisine, par la méthode seule. Sans rapport avec l'objet de H2.**

- À noter, dans le sens de la précaution du programme sur la puissance : **[Q40]** `2606.08106v1.pdf` p. 5 : « What the guarantee does not control is power »

### 2.6 2609.10739v2 — « The Truth Was Never Gone: Perfect Aliasing in Compliant-Context Truth Probes »

Dylan Jayabahu (Université de Waterloo) ; 8 octobre 2026 (page 1).

**Ce qu'elle fait.** Dans un jeu contrôlé (dire un bit secret à un allié, son complément à un rival), une sonde de vérité ajustée sur les seuls contextes honnêtes ne peut pas distinguer « la vérité » de « la réponse prescrite » : les deux étiquettes y sont identiques. Sur les contextes trompeurs, elle s'inverse, alors que le bit reste lisible linéairement.

- **[Q41]** `2609.10739v2.pdf` p. 1 : « On compliant (ally) contexts the true bit and the answer the task prescribes are identical labels, so a probe fitted there cannot tell which of the two it measures. »
- **[Q42]** `2609.10739v2.pdf` p. 1 : « the ally-fitted probe scores 0.006 ± 0.005 AUROC at the final layer »
- **[Q43]** `2609.10739v2.pdf` p. 1 : « while mixed-fit probes score 1.000 on the same held-out activations »
- **[Q44]** `2609.10739v2.pdf` p. 4 : « A below-chance truth/ally is therefore what a prescribed-answer reading predicts; on its own it does not show that truth information was removed. »

**Contre H8.** H8 dit : le construit réellement mesuré (intention contre conscience d'évaluation) prédit la robustesse adverse ; le programme écrit que le glissement de construit est déjà décrit et que seule la prédiction ne l'est pas. Cette pièce donne un cas exact où l'identité du construit **décide** de la lecture hors du contexte d'ajustement (les deux aires sous la courbe somment à un, p. 4). C'est le socle. Elle ne donne **pas** la prédiction :

- pas d'attaquant, pas de robustesse adverse ; pas de conscience d'évaluation ; un jeu à un seul jeton ;
- elle dit ne pas pouvoir prédire quel construit un ajustement adopte : **[Q45]** `2609.10739v2.pdf` p. 8 : « Neither the deception rate nor mean rival-answer entropy (over the two legal answers) orders the readouts across arms »
- elle borne sa propre portée : **[Q46]** `2609.10739v2.pdf` p. 2 : « We neither dispute nor reproduce the failures above, so we do not show that they arise from perfect aliasing »
- elle ne revendique pas l'objection générale : **[Q47]** `2609.10739v2.pdf` p. 9 : « We do not claim the general identification objection is new »
- **[Q48]** `2609.10739v2.pdf` p. 9 : « The label structure, remedy and recommendations are untested on long-form deception. »

**Verdict : occupe en partie H8** — composante « l'ambiguïté du construit explique l'échec d'une sonde hors de son contexte d'ajustement » (p. 1, [Q41] ; p. 4, [Q44]), qui est le socle non revendiqué. La pièce revendiquée (prédiction de la robustesse adverse par le construit) : **libre dans cette pièce**. Le résultat négatif [Q45] est un signal faible **contre** la facilité de la prédiction : deux prédicteurs simples du comportement ont échoué.

**Contre H1 et H2 : contre-résultat.** Une sonde ajustée sur les seuls contextes honnêtes, validée à 1,000 sur ces contextes, peut lire à l'envers sous tromperie. Le remède demande des exemples trompeurs étiquetés.

- **[Q49]** `2609.10739v2.pdf` p. 9 : « Mixed fitting needs labelled deceptive examples, which a monitor for a policy that has not yet been caught may not have; our results do not show how to identify a truth probe without them. »
- **[Q50]** `2609.10739v2.pdf` p. 9 : « establishing what a probe measures requires evaluation cases in which the candidate targets disagree »

Conséquence à connaître, sans rien changer aux énoncés : H2 retenue dit « seuil calibré sur des épisodes honnêtes, sans aucun exemple de sabotage ». Cela porte sur le **seuil**. Si la **sonde** elle-même n'est ajustée que sur des contextes où l'étiquette visée et une étiquette voisine coïncident, cette pièce montre qu'une validation parfaite en distribution ne protège pas. Une seconde mise en garde : la section 5 de la pièce (figure 3, p. 6) montre que réajuster une sonde par condition fabrique des écarts qu'une sonde gelée ne montre pas (0,080 contre 0,986 sur les mêmes essais, résumé p. 1).

Sur la transposition jeton → action : la pièce ne fait que citer le résultat de départ (p. 2, Gupta et Jenner, 2025 : agrégations par maximum et par attention robustes). Elle n'y touche pas.

### 2.7 2607.13346v2 — « PRISM: Stress-Testing Alignment-Faking Claims » (signalée sous le titre « The Refusal Residue »)

Aman Mehta (Snowflake AI Research) ; version 2 du 5 novembre 2026 ; acceptée à un atelier d'interprétabilité mécaniste de la conférence ICML 2026 (page 1).

- **[Q51]** `2607.13346v2.pdf` p. 1 : « PRISM: Stress-Testing Alignment-Faking Claims »

**Ce qu'elle fait.** Elle teste deux inférences sur l'« alignement simulé » des modèles ouverts : que l'écart d'obéissance sous consigne « surveillé » vient de la menace d'entraînement, et qu'une sonde sur les états cachés le détecte. Les deux tombent. Par un plan factoriel de consignes, l'écart suit le libellé de la consigne. Par un contrôle apparié, la sonde sépare aussi bien les refus, où aucune simulation n'est possible.

- **[Q52]** `2607.13346v2.pdf` p. 1 : « they separate refusals just as well: they read the prompt, not the faking »
- **[Q53]** `2607.13346v2.pdf` p. 4 : « A two-layer MLP then separates monitored from unmonitored compliant answers with AUROC 0.96 (Llama) and 0.99 (Qwen), and refusals with 1.00 (Llama) and 1.00 (Qwen) »
- **[Q54]** `2607.13346v2.pdf` p. 7 : « Probes and steering directions for “faking” in this setup are dominated by which prompt the model saw. »

**Contre H8.** C'est une démonstration de contamination de construit, précisément sur l'axe que H8 nomme (intention contre conscience d'évaluation). Elle l'étend aux sondes de conscience d'évaluation publiées :

- **[Q55]** `2607.13346v2.pdf` p. 7 : « a probe that separates evaluation from deployment prompts must also be shown not to separate them for behavior that cannot depend on awareness »
- **[Q56]** `2607.13346v2.pdf` p. 7 : « A bag-of-words classifier on the same sentences reaches 96.5% on a split rebuilt from their released code »

(La sonde publiée qu'elle réexamine annonçait 95,1 % ; p. 7.)

Elle ne mesure aucune robustesse adverse et ne prédit rien à partir du construit.

**Verdict : occupe en partie H8** — composante « la sonde lit la consigne, pas l'intention » (p. 1, [Q52] ; p. 4, [Q53] ; p. 7, [Q55]) : socle non revendiqué, et le contrôle par les refus est une méthode publiée à citer et à reprendre. La pièce revendiquée (prédiction) : **libre dans cette pièce**.

**Contre H1 : contre-résultat, à deux faces.**

- Face défavorable : un gain apparent des états cachés sur le texte peut n'être que la lecture de la consigne. Ici les classifieurs de texte plafonnent bas alors que les états cachés séparent presque parfaitement — et ce qu'ils séparent n'est pas la propriété visée. **[Q57]** `2607.13346v2.pdf` p. 4 : « text classifiers on the same answers reach at most 0.68 (Llama) and 0.61 (Qwen) »
- Sur la sonde de conscience d'évaluation réexaminée, un sac de mots fait aussi bien que la sonde ([Q56]) : pas de gain blanc sur noir.
- Règle générale posée par la pièce : **[Q58]** `2607.13346v2.pdf` p. 2 : « In each case the two classes come from different inputs, so a probe can succeed by reading the input. »

Le programme a déjà une parade inscrite (N-053 : famille d'organismes sans texte de consigne ; N-029 : prédicteur sur les traits du texte obligatoire). Cette pièce en est la justification publiée la plus nette que j'aie lue ; elle ajoute un contrôle que je n'ai pas vu dans les décisions lues : rejouer le même contraste sur un comportement où la propriété visée ne peut pas se produire.

### 2.8 Sources classiques du lemme

#### 1810.08240v9 — « Time-uniform, nonparametric, nonasymptotic confidence sequences »

Steven R. Howard, Aaditya Ramdas, Jon McAuliffe, Jasjeet Sekhon ; version 9 du 6 août 2022 (page 1).

- **[Q59]** `1810.08240v9.pdf` p. 1 : « A confidence sequence is a sequence of confidence intervals that is uniformly valid over an unbounded time horizon. »

**Énoncés exacts qui servent de source à la borne de mélange.**

1. **Condition de départ** : définition 1 (« condition sous-ψ »), p. 5.
2. **Méthode des mélanges** : lemme 2, équation (13), p. 9. Les auteurs la disent classique : **[Q60]** `1810.08240v9.pdf` p. 9 : « We restate the following standard idea behind the method of mixtures using our definitions »
3. **Mélange normal bilatéral** : équation (14), p. 10 ; proposition 5, équation (51), p. 28. Dit connu : **[Q61]** `1810.08240v9.pdf` p. 28 : « In the sub-Gaussian case, the following boundary is well-known (Robbins, 1970, example 2). »
4. **Mélange normal unilatéral** : proposition 6, équations (52) et (53), p. 28. **[Q62]** `1810.08240v9.pdf` p. 28 : « Proposition 6 (One-sided normal mixture). For any α ∈ (0, 1) and ρ > 0, the boundary » — puis : **[Q63]** `1810.08240v9.pdf` p. 28 : « is a sub-Gaussian uniform boundary with crossing probability α »
5. **Inégalité de Ville** dans la preuve du lemme 2 : **[Q64]** `1810.08240v9.pdf` p. 28 : « Ville’s maximal inequality for nonnegative supermartingales »
6. **Choix du paramètre ρ** pour un horizon visé : proposition 3, équation (21), p. 12, en forme close (fonction de Lambert). **[Q65]** `1810.08240v9.pdf` p. 12 : « it is a matter of elementary calculus, but addresses a question that has received little attention in the literature »
7. **Impossibilité d'améliorer** la borne de mélange en général : proposition 4, équation (22), p. 13.

**Concordance avec la note mathématique v3 (`docs/notes/note-mathematique-lemme-theoreme-v3.md`, section 2).** Mon calcul, non relu par un tiers : les deux formules de la note (bilatérale et unilatérale) sont celles des propositions 5 et 6 avec l₀ = 1 et le changement de paramètre ρ (Howard) = 1/ρ² (note). La note fixe ρ « comme minimiseur numérique de la frontière à l'horizon n₀ » : la proposition 3 de Howard donne ce minimiseur en forme close pour le cas bilatéral ; à citer, pas à revendiquer.

**« La puissance ne dépend que du budget total, pas de sa répartition » : non.** L'article ne traite que le risque de première espèce. La puissance n'y apparaît que comme « test de puissance un » :

- **[Q66]** `1810.08240v9.pdf` p. 19 : « will yield a test of power one (Darling and Robbins, 1967b; Robbins, 1970) »

Aucun des mots « budget », « allocation » n'y a de sens de sabotage ou de répartition d'un signal (recherche par mots sur les 48 pages ; lecture ligne à ligne des seules pages listées en section 1).

**Verdict : source classique de la borne de mélange, portée sur PDF. N'occupe rien de ce que le lemme revendique.** La « piste, non vérifiée » de C2 et de C6 sur cette source est levée pour les points 1 à 7.

#### 1007.1434v2 — « Global testing under sparse alternatives: ANOVA, multiple comparisons and the higher criticism »

Ery Arias-Castro, Emmanuel J. Candès, Yaniv Plan ; The Annals of Statistics, 2011, volume 39, numéro 5 ; version 2 du 23 février 2012 (page 1).

**Énoncés exacts qui servent de source à la dichotomie somme contre maximum.**

1. **Le test de somme (analyse de variance, somme des carrés) et son optimalité contre un budget quadratique total.** Page 2 : le test rejette pour de grandes valeurs de la somme des carrés ; **[Q67]** `1007.1434v2.pdf` p. 2 : « maximizes the minimum power against alternatives of the form » — la forme est l'ensemble des vecteurs dont la somme des carrés dépasse B (les auteurs emploient la lettre B). Ils ajoutent : **[Q68]** `1007.1434v2.pdf` p. 2 : « Such an appealing property may be shown via invariance considerations; see [32] and [28], Chapters 7 and 8. »
2. **Le test du maximum et son avantage quand le signal est concentré.** **[Q69]** `1007.1434v2.pdf` p. 3 : « ANOVA requires A to be at least as large as p1/4 to provide small error probabilities, whereas the Max test only requires A to be on the order of (2 log p)1/2 »
3. **Les configurations les plus dures pour chacun.** **[Q70]** `1007.1434v2.pdf` p. 3 : « the likelihood functions are hard to distinguish when the entries of β are of about the same size (in absolute value) » ; et pour le maximum : **[Q71]** `1007.1434v2.pdf` p. 3 : « the likelihood functions are hard to distinguish when there is a single nonzero coefficient equal to ±A »
4. **Loi exacte de la statistique de somme sous l'alternative.** **[Q72]** `1007.1434v2.pdf` p. 6 : « has the chi-square distribution with min(n, p) degrees of freedom and » — suite page 7 : **[Q73]** `1007.1434v2.pdf` p. 7 : « noncentrality parameter » — ce paramètre est la norme au carré de Xβ ; condition (1.7), p. 7.
5. **Théorèmes.** Proposition 1, p. 12 (aucun test n'est puissant sous le seuil, régime dense). Théorème 1, p. 13 : **[Q74]** `1007.1434v2.pdf` p. 13 : « Also, the Max test is asymptotically powerful if r > ρMax (α) and powerless if r < ρMax (α). » Théorème 5, p. 17-18 (même énoncé pour des plans faiblement corrélés). Synthèse : **[Q75]** `1007.1434v2.pdf` p. 13 : « In contrast, the Max test is only optimal in the range α ≥ 3/4. »

**« La puissance ne dépend que du budget total, pas de sa répartition » : pas écrite comme phrase ; portée en substance, sous une autre forme.** Par [Q72] et [Q73], la statistique de somme suit sous l'alternative une loi du khi-deux décentrée dont le seul paramètre qui dépende du signal est la norme au carré de Xβ. Pour un plan orthogonal, c'est la somme des carrés des coefficients (p. 12 : « kXβk2 = kβk2 », lu, non cité au contrôle à cause des symboles). **Inférence de ma part, immédiate** : la puissance du test de somme ne dépend donc du signal que par ce total, pas par sa répartition entre coordonnées. C'est l'analogue classique de L1, avec quatre différences :

- le budget est **quadratique** (somme des carrés), celui du lemme est **linéaire** et de signe fixé (somme des décalages) ;
- l'horizon est **fixe** : aucune lecture séquentielle, aucune garantie valable à tout instant, donc rien de L3 (calendrier, coût du report, prix de la garantie) ;
- aucun adversaire qui choisit la répartition ;
- aucune indexation par agents et pas de temps.

**Verdict : source classique de L2, portée sur PDF. Pour L1, parenté classique confirmée : l'invariance d'une statistique de somme au seul total du signal est connue sous sa forme quadratique à horizon fixe (p. 2, 6-7), sans être énoncée comme telle.** Cela confirme la lecture de C2 (« libre dans les pièces lues ; élémentaire ») et de N-004 (« le cœur statistique est cité comme classique »). Cela n'occupe pas l'énoncé adverse séquentiel.

**Deux points de cette source qui jouent contre une présentation trop simple du lemme.**

- La dichotomie n'est pas à deux termes. Entre le régime dense et le régime très rare, ni la somme ni le maximum ne sont optimaux : **[Q76]** `1007.1434v2.pdf` p. 1 : « these two very popular methods are suboptimal, and sometimes powerless, under moderately strong sparsity where 1/2 < α < 3/4 » — et un troisième agrégateur (la critique supérieure) est puissant sur toute la plage rare (p. 1, p. 13). Un jury statisticien demandera pourquoi le plan « somme contre maximum » n'a pas ce troisième bras. Le programme ne le revendique ni ne l'exclut ; je le signale.
- Quand le signal est concentré, le maximum bat la somme de loin ([Q69]). C'est cohérent avec L1 (« à B fixé, la puissance décroît avec n₀ ») et L2, mais cela rappelle que l'avantage de la somme n'existe que si le saboteur **étale**.

Réserve : ces résultats sont asymptotiques, bilatéraux, gaussiens. Le cas du lemme (décalages positifs, somme unilatérale) relève du modèle de moyenne rare de Donoho et Jin (référence [9] de l'article), absent du dépôt à ma connaissance : piste, non vérifiée.

## 3. H2, composante par composante

Énoncé retenu (N-007) : sur des trajectoires où chaque action sabotée reste sous le seuil d'un moniteur par action calibré à 1 % de fausses alarmes, l'accumulation additive toujours valide de scores de sondes de l'agent qui agit détecte le sabotage avec un rappel qui croît avec l'horizon ; seuil calibré sur des épisodes honnêtes, sans exemple de sabotage.

| Composante | 2606.12476 (Itkin) | 2608.02464 (Dubey) | 2608.27808 (CURA) | 2607.20129 (MGT-B) | 2606.08106 (PACE) |
|---|---|---|---|---|---|
| (1) Scores de sondes internes | non : texte et probabilités de sortie (p. 3) | non : télémétrie (p. 2) | non (p. 1) | non : logits de sortie (p. 2) | non (p. 2) |
| (2) De l'agent lui-même | sans objet (un générateur de texte, pas un agent) | l'agent est observé du dehors | l'agent est observé du dehors | le modèle lui-même, par sa sortie | sans objet |
| (3) Accumulation séquentielle | oui : somme de Page apprise (p. 1, 5) | **oui : somme de Page (p. 4)** | **oui : somme de Page (p. 4)** | oui, « en forme de » (p. 1) | oui : processus e, autre objet (p. 4) |
| (4) Garantie de fausse alarme valable à tout instant | non : longueur moyenne mesurée (p. 4) | non : quantile empirique du maximum sur épisodes sains (p. 4) | **oui : certificat en échantillon fini (p. 3, 4) et variante de Ville (p. 4, 16)** | non, écrit (p. 2, 3) | oui, par candidat (p. 5) |
| (5) Sabotage diffus, chaque action sous le seuil par action | non : hallucination | non : pannes ; « dérive lente » dite, non mesurée ainsi (p. 4, 12) | non : échecs non adverses (p. 1, 7) | non | non |
| (6) Rappel croissant avec l'horizon | non | en partie : gain croissant avec l'horizon après le début (p. 5) | non trouvé | non | non |

**Lecture.** Dans ce lot, (3) et (4) sont réunies sur des trajectoires d'agent par CURA, avec un calibrage sans exemple négatif. C'est en boîte noire et hors menace adverse. Aucune pièce de ce lot n'a (1), ni (5). Jointe au tableau de C1 (où SafeDream réunit (1), (2), (3) sans (4) ni (5)), la conjonction non trouvée reste : **scores de sondes de l'agent** et **garantie uniforme sur l'horizon calibrée sur épisodes honnêtes** et **sabotage par l'agent sous le seuil par action**. Chaque moitié a désormais un titulaire publié distinct (SafeDream pour le signal interne accumulé, CURA et E-valuator pour la garantie). Un jury peut dire que H2 est leur produit ; la réponse tient à (5) et à (6), et à la mesure.

## 4. Synthèse par énoncé (dans les pièces de ce lot seulement)

| Énoncé | Verdict | Appui |
|---|---|---|
| H1 | libre dans ce lot ; deux contre-résultats de validité | 2607.13346, p. 2, 4, 7 ; 2609.10739, p. 1, 9 |
| H2 (énoncé retenu) | occupée en partie, en boîte noire : (3), (4), calibrage sans exemple négatif, par CURA (p. 1, 3, 4, 16) ; (3) et (6) en partie par 2608.02464 (p. 4, 5) | section 3 |
| Lemme, borne de mélange | classique, source portée | 1810.08240, p. 9, 10, 28 |
| Lemme, L1 (invariance au budget) | libre comme énoncé adverse séquentiel ; parenté classique confirmée en forme quadratique à horizon fixe | 1007.1434, p. 2, 6-7 |
| Lemme, L2 (somme contre maximum) | classique, source portée ; la forme exacte de L2 (seuil exact, plancher au-dessus de α à n fixé) n'y est pas | 1007.1434, p. 3, 13, 17-18 |
| Lemme, L3 (calendrier, coût du report, prix de la garantie) | libre dans ce lot ; un point empirique du prix de la garantie chez CURA (p. 5), non chiffré comme tel | 2608.27808, p. 5 |
| Théorème négatif | libre dans ce lot ; le principe d'invariance est rappelé comme classique | 1007.1434, p. 2 [Q68] |
| H6 | libre dans ce lot | aucune pièce n'en traite |
| Transposition jeton → action | libre dans ce lot | 2609.10739 cite seulement le résultat de départ (p. 2) |
| H8, socle (contamination de construit) | occupé en partie, non revendiqué | 2609.10739, p. 1, 4 ; 2607.13346, p. 1, 4, 7 |
| H8, pièce revendiquée (prédiction de la robustesse) | libre dans ce lot ; signal faible contre sa facilité | 2609.10739, p. 8 [Q45] |

**Réserve (R4).** Le tableau est propre parce que le lot est étroit et que cinq des neuf pièces sont en boîte noire par construction. Il ne dit rien des pièces non lues.

## 5. Contre-résultats défavorables au programme

1. **L'accumulation pèse peu face à la qualité du score par pas** (2606.12476, p. 1 et 2, [Q07], [Q08]) : environ un quart du gain, à fausse alarme égale, sur un autre phénomène. Si la même décomposition vaut pour des scores de sondes, le gain de H2 sur la base « dernier état » ou « par action » pourrait être modeste. La décomposition elle-même (score linéaire, score non linéaire sans séquence, puis accumulation) est un plan de contrôle à reprendre.
2. **À fausse alarme faible, le rappel est bas partout** (2606.12476, p. 1, [Q09] ; 2608.27808, p. 1 : 42,3 % à α = 0,10, [Q25]). Les chiffres publiés de détection séquentielle sous garantie sont loin de 1.
3. **Les seuils calibrés sur du sain ne se transportent pas** (2608.02464, p. 5 et 10, [Q17], [Q18] ; 2608.27808, p. 7, [Q30]). La garantie ne vaut que sous la loi calibrée ([Q29]). Pour H2 : « toujours valide » ne survit pas à un changement de modèle, de tâche ou de température sans recalibrage.
4. **La dérive lente échappe à la somme cumulée en boîte noire** (2608.02464, p. 12, [Q16]). C'est la menace même de H2 ; le programme parie que le signal interne la voit. Rien dans ce lot ne le montre.
5. **Une base triviale de longueur résiste** (2608.27808, p. 1). À inscrire parmi les planchers rapportés de G1 si elle n'y est pas.
6. **Une sonde ajustée sur contextes honnêtes peut s'inverser sous tromperie, tout en étant parfaite en validation** (2609.10739, p. 1, 4, 9, [Q41] à [Q44], [Q49]).
7. **Une sonde peut lire la consigne, pas la propriété** ; un sac de mots égale une sonde de conscience d'évaluation publiée (2607.13346, p. 1, 4, 7, [Q52], [Q56]). Contre H1 si le gain blanc sur noir n'est pas contrôlé par un comportement où la propriété ne peut pas se produire.
8. **La dichotomie somme contre maximum a un troisième terme classique** (1007.1434, p. 1, [Q76]) ; et l'invariance de la somme au seul total est de parenté classique (p. 2, 6-7). L'originalité de L tient à l'énoncé adverse séquentiel et à la mesure, pas à L1 ni à L2 pris seuls — ce que N-004 écrit déjà.
9. **Le prix de la garantie valable à tout instant est observé** (2608.27808, p. 5, [Q24]) : la variante de Ville tire plus tôt mais sur moins d'échecs.

## 6. Pièces à lire ou à récupérer (pistes, non vérifiées, R7)

Présence au dépôt vérifiée par `ls` du chemin exact `docs/sources/pdf/<identifiant>v*.pdf`.

| Pièce | État | Pourquoi |
|---|---|---|
| Robbins (1970), « Statistical methods related to the law of the iterated logarithm », exemple 2 ; Robbins et Siegmund (1970) | hors dépôt, sans identifiant arXiv | source première de la borne de mélange normal, selon Howard p. 10 et 28 |
| Donoho et Jin (2004), critique supérieure ; Ingster ; Hall et Jin (bruit corrélé, séries temporelles) | hors dépôt | modèle de moyenne rare unilatéral (le cas du lemme) ; critique supérieure sous dépendance (références [9], [22], [18], [19] de 1007.1434) |
| 2606.07624, Xie, « Sequential statistical inference for large language models: Representation, validity, and monitoring » | absent | cité par 2606.12476 (p. 2) comme plaidoyer pour les alarmes séquentielles sur modèles déployés ; le mot « representation » du titre appelle une lecture contre H2 |
| 2602.11409, Tayebati et collègues, « TRACER: Trajectory Risk Aggregation for Critical Episodes in Agentic Reasoning » | absent | même équipe que CURA ; agrégation du risque le long d'une trajectoire d'agent |
| 2606.05414, Baidya et collègues, alerte précoce faiblement supervisée | absent | cité par 2608.02464 (p. 2) : risque par tour appris d'étiquettes de trajectoire |
| 2601.00516, Advani, « Trajectory Guard » | absent | cité par 2608.02464 (p. 2) : anomalies de trajectoire sans étiquettes |
| 2602.01425, Natarajan et collègues, « One probe won't catch them all » | absent | cité par 2609.10739 : 70,6 % de la variance de l'aire sous la courbe des sondes attribuée au contraste de consigne d'ajustement (chiffre de seconde main, non opposable) ; voisin possible de la **prédiction** de H8 |
| 2507.20836, Snel et collègues | absent | premier jeton d'une hallucination plus détectable que la suite ; voisin lointain |
| 2602.15515 (« The obfuscation atlas ») ; 2605.06455 (PrefixGuard) ; 2607.06503 (*Doomed from the Start*) | **présents** au dépôt | cités par les pièces de ce lot ; je ne les ai pas lus et ne sais pas si un lot les couvre |
| Version 1 de 2607.13346 | absente | vérifier si le titre « The Refusal Residue » est celui de la version 1, et si le contenu a changé |

## 7. Contrôle des citations et refus

- Essai préalable du script (R5) : cas juste accepté ; cas altéré rejeté ; mauvaise page rejetée.
- Compte final : voir la ligne ci-dessous, recopiée de la sortie du script.

`citations contrôlées : 76 ; échecs : 0 ; clés en double : [] ; marques non analysées : []`

- Refus rencontrés : aucun.
- Aucun appel de modèle, aucune requête sur le réseau, aucune branche ouverte, aucun fichier écrit hors de ce rapport, de son empreinte compagnon et du dossier temporaire.

## 8. Limites de ce rapport

- Lecture partielle, détaillée en section 1.
- Les empreintes des huit pièces neuves sont celles des fichiers du dossier temporaire ; je ne les ai pas rapprochées des fichiers compagnons de la branche de préparation.
- La concordance entre les formules de la note mathématique v3 et les propositions 5 et 6 de Howard est mon calcul, à faire relire.
- L'inférence « la puissance du test de somme ne dépend que du total quadratique » (section 2.8) est de moi ; l'article donne la loi, pas la phrase.
- Les verdicts « occupe en partie » de la section 2.6 et 2.7 portent sur le socle de H8, que le programme dit déjà décrit. Un lecteur plus strict écrirait « voisine » ; j'ai retenu « occupe en partie » parce que les deux pièces doivent être citées et que l'une touche l'axe exact nommé par H8.
