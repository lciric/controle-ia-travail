# Propositions d'essais pour l'organisme d'idéation, tirées de Re-Search (arXiv 2611.14487 v1) — v1

- Rédacteur : modèle I (rédacteur neuf, session du compte organisme). Rédigé le 2026-11-18T04:29:39Z (`date -u` dans la commande de rendu).
- Statut : **propositions, rien d'adopté**. La note de conception de la suite est suspendue par la mère ; chaque proposition est un essai à décider par Lazar, avec son devis ; aucun lancement, aucune dépense, aucun appel de modèle n'a été fait pour cette note. Rien ici ne change une hypothèse ni une revendication.
- Pièces lues (empreintes recalculées au rendu) : table de décision `table-decision-re-search-v1.md` (0ccba06e…) ; lecture `lecture-re-search-v1.md` (21d00c6d…) et ses citations (94 sur 94) ; analyse `analyse-journaux-re-search-v1.md` (8a82b5ee…) et sa sortie `analyse-journaux-re-search-v1-sortie.json` (3b65a5e8…) ; décisions N-044 v1, N-045 v2, N-049 v1, N-058 v1, N-065 v1 (`docs/decisions/`) ; dépôt public de l'organisme (lecture seule, commit a41b7b5) : `README.md` sections 1 à 3 et 7 (04ac692e…), `orchestrator/pole/memoire.py` (71f1d086…) en entier pour P2, et l'en-tête de `orchestrator/pole/bisociateur_v55.py` (d9521311…), qui ne porte que sur l'annexe du bras méta (aucune proposition ne le change).
- Table remplie : `propositions-conception-re-search-v1-table-remplie.md` (même dossier). Pièce de l'article : PDF sha256 `ae848c68e65c4a779d0df6725e4189ad80c351fe2e9402930be14db2ddfa7ccc`. Chaque passage entre guillemets français de cette note est un passage de `propositions-conception-re-search-v1-citations-pdf.json`, sous son identifiant [PC-nn] et sa page du PDF (1 = première page) ; vérifié par programme au rendu.
- Chemins JSON entre accents graves : dans la sortie d'analyse ci-dessus, sauf mention.
- Convention : aucun nom de modèle de la famille du rédacteur n'est écrit ; les proposeurs de nos journaux sont nommés comme dans la sortie d'analyse (argon, kimi).

## Verdict d'abord

Une ligne de la table change (C3 : mode dominant de répétition de formes dans nos journaux) ; les quatre autres sont indécidables avec ce qu'on a (C1, C2, C4, C5). Trois essais sont proposés, tous jugés sur l'oracle d'un monde planté et le coût, jamais sur un verdict de juge (N-058), et tous précédés d'une phase sans dépense (N-045 v2, point 4) :
- **P1** (C5, et mesure sur la vérité pour C1 et C3) : un jeu de questions fermées où le répondeur est le monde planté lui-même. Phase 0 : 0 USD ; phase 1 : pire cas 267,84 USD.
- **P2** (C3) : une mesure de la forme dans la mémoire, puis un indice de diversification essayé contre la mémoire actuelle. Phase 0 : 0 USD ; phase 1 : pire cas 68,63 USD.
- **P3** (C2 et C4) : des candidats offerts au questionneur, montés sur l'instrument de P1. Phase 0 : 0 USD ; phase 1 : pire cas 200,88 USD ; phase 2 : pire cas 370,05 USD.

## 0. Ce qui borne toutes les propositions

1. **Aucun modèle ne décide d'une promotion** (README, section 1 : le rôle qui produit un artefact ne tient jamais la clé qui l'évalue ; la promotion est décidée par le juge statistique, écrit dans le code de l'orchestrateur). Dans l'article, le répondeur et les juges sont des modèles : « In all games, Gemma-4-31B serves as the answerer, each inquisitor asks up to T = 100 questions, and we play three games per paper. » [PC-19, p. 5] ; « Recovery scores come from a panel of three LLM judges, and the search trees are annotated by an LLM. » [PC-11, p. 9]. Rien de leur chaîne de jugement n'est repris.
2. **La composition des proposeurs se juge sur l'oracle du monde planté et le coût, seuls** (N-058, point 1) ; le classement des juges croisés et les promotions du juge statistique n'entrent dans aucun critère ci-dessous, sauf qualifiées par l'oracle (témoins vrais promus, faux rejetés), comme N-058 le définit.
3. **Les témoins plantés du pôle ne sont jamais servis aux agents** (README, section 3, ligne des témoins ; `memoire.py` l. 3-5). Les mondes des instruments proposés sont donc tirés à part, disjoints des témoins et des mondes de production, et jamais servis dans la boucle.
4. **Le bon marché d'abord** (N-045 v2, point 4) : chaque essai commence hors ligne, simulé ou avec des proposeurs factices ; une phase payante n'est demandée qu'après lecture de la phase gratuite.
5. **Tâches fraîches** (N-049) : chaque partie d'un instrument tire un monde neuf d'un générateur (graine dérivée de `SeedSequence(20261118)`, R9) ; une banque de confirmation scellée, lue une fois, et une famille de lois tenue à l'écart de la conception (N-044, point 1) servent aux lectures décisives.

## P1 — Instrument : le monde planté répond (ligne C5 ; mesure sur la vérité pour C1 et C3)

**Ce que cela change, et où.** Aucun module de la table 2 du README n'est changé. C'est un instrument neuf, hors de la boucle de production (fichier nouveau, versionné, R12), qui réutilise la grammaire fermée des lois de nos mondes jouets (types relevés par l'analyse : softmax, transformée, mélange, si_sinon, par sous-population, `S1.M1.*.par_proposeur.*.types`) et une divergence calculée sur une sonde fixe, comme celle de la mémoire (`memoire.py` l. 9-12 et 156-160 : divergence de Kullback-Leibler moyenne sur une sonde de 256 instances).

**Le jeu.**
- Un monde : une loi tirée par le générateur dans la grammaire, disjointe des témoins et des mondes de production (garde de disjonction par la signature prédictive, comme la mémoire).
- Le questionneur (un proposeur) pose jusqu'à T = 16 questions fermées, prises dans une grammaire de prédicats écrite et scellée avant tout monde. Variante principale : prédicats **empiriques** seulement (par exemple : sous la loi du monde, la probabilité de l'issue a quand le trait j dépasse s est-elle plus haute que quand il ne le dépasse pas ?), calculés exactement par le code sur la loi du monde ou sur une grande sonde fixe. Variante rapportée à part : prédicats **structurels** (la loi dépend-elle du trait j ? le nœud racine est-il un mélange ?), plus faciles et plus éloignés de la recherche réelle.
- Réponse Oui ou Non, calculée par le code : la vérité par construction. Une question hors grammaire est refusée et comptée, jamais répondue Inconnu.
- Après les questions 4, 8 et 16, le questionneur écrit une loi dans la grammaire (sa carte). Score : divergence moyenne de la loi du monde à la carte sur la sonde, et égalité de forme, calculées par le code. Aucune note d'un modèle.

**Pourquoi l'article et nos données le suggèrent.** La faiblesse de construction de l'article tient à trois maillons modèles (table remplie, ligne C5) : « Gemma agrees most often with human labels on 795 annotated answers (94.0%, against 86.2% for GPT-OSS-120B and 78.4% for Qwen3.6-35B-A3B; see § D for details), and only 1.1% flip YES and NO » [PC-14, p. 5] ; « checked the extracted pairs (p, s) for 100 papers. By majority vote, 93% are correct, and the errors mostly omit a component that distinguishes the paper's method. » [PC-15, p. 4] ; « by comparing 498 pairs of idea cards; for each pair, they choose the card closer to the hidden solution, or mark a tie. Their labels agree well, with a Fleiss' κ of 0.83. In 91.2% of pairs, the LLM judges agree with the annotator majority on which card is closer, or that the two are tied. » [PC-17, p. 4] ; et la carte ne monte qu'au rythme des Oui, « write "Not recovered from the transcript" unless at least one Yes answer directly supports that field » [PC-02, p. 24]. Un monde qui répond supprime les trois maillons. Côté nos journaux, la mesure sur la vérité manque partout : en S1, la vérité n'est écrite que pour les cartes promues, agrégée par proposeur (écart E2 de l'analyse) ; en S2, l'événement est le verdict du juge et l'arrêt au premier succès crée un effet de composition entre cases (analyse, section 3). Dans le jeu proposé, chaque partie joue ses 16 questions sans arrêt au premier succès : le rendement tardif contre précoce (ligne C1) se mesure dans une même partie, sur la vérité.

**Ce qui reste différent entre leur cadre et le nôtre.** Leur cible est la méthode d'un article, en langue naturelle ; la nôtre est une loi dans une grammaire fermée, bien plus étroite. Leur répondeur lit l'article et la carte de solution, « evidence (the hidden solution card and the full paper) » [PC-16, p. 16] ; le nôtre calcule. Leur score est un panel de modèles ; le nôtre une divergence. L'instrument ne promeut rien : il mesure la recherche par questions des proposeurs, pas la production de cartes du pôle ; ses chiffres ne valent pour la boucle qu'après un essai de lien entre les deux (non proposé ici). Une question empirique fine révèle beaucoup de la loi : c'est voulu (on mesure la recherche), et la borne d'information reste de T bits pour T questions Oui ou Non.

**Mesures.** M-P1a : divergence à T = 16, par questionneur. M-P1b : rendement sur la vérité, baisse de divergence entre les questions 0 à 4 et entre 5 à 16, par partie (analogue de C1, sans effet de composition). M-P1c : information par question, quand l'ensemble des lois compatibles est énumérable. M-P1d : arbre des questions calculé par le code (prédicats sur les mêmes traits ou nœuds), part de questions qui raffinent la précédente et nombre de directions ouvertes (analogue de C3, sans annotateur modèle). M-P1e : coût par partie.

**Phase 0 (sans dépense : processeur seul).** Code du jeu, puis quatre questionneurs factices : aléatoire dans la grammaire ; bissection gloutonne par gain d'information sur l'ensemble énuméré des lois candidates ; répéteur (toujours le même trait) ; disperseur (jamais deux fois le même trait).
- Hypothèse de validité de l'instrument : sur 200 mondes neufs, à T = 16, ordre strict des divergences médianes : bissection < aléatoire < répéteur ; chaque écart a un intervalle à 95 % (10 000 rééchantillonnages des mondes, `SeedSequence(20261118)` dérivée par tâche) qui exclut 0.
- Critère fixé d'avance : si l'ordre ne tient pas, l'instrument ne mesure pas la recherche ; arrêt, rapporté, aucune phase 1.
- Essais R5 : cas sain (valeurs calculées à la main sur un monde à deux traits) ; artefacts : un répondeur qui inverse 10 % des réponses doit faire perdre la bissection (intervalle qui exclut 0) ; un répondeur qui fuit la loi doit être détecté (recouvrement parfait au premier tour signalé et refusé).

**Phase 1 (dépense, sur devis).** Les deux proposeurs réels de la course v67 (argon, kimi) comme questionneurs, 8 mondes neufs, deux parties par proposeur et par monde (test A/A, N-045 v2, point 6 i).
- Critère fixé d'avance : (i) A/A : l'écart entre les deux parties d'un même proposeur a un intervalle à 95 % qui contient 0, sinon l'instrument est trop bruité à cette taille (rapporté, aucune lecture de composition) ; (ii) la position de chaque proposeur entre les bornes factices (aléatoire, bissection) est rapportée avec son intervalle. Aucune décision de composition dans cette phase : information ; une décision de composition sur cet instrument exigerait son propre préenregistrement (la mesure est bien l'oracle du monde planté et le coût, N-058).
- Bras témoins : questionneurs factices aléatoire et bissection sur les mêmes mondes (sans coût) ; A/A.
- Confirmation (plus tard, hors de ce devis) : banque de mondes scellée, lue une fois, et une famille de lois tenue à l'écart (N-044, N-049).

**Devis.**

| poste | appels | prix unitaire et source | estimation | pire cas |
|---|---|---|---|---|
| phase 0 | 0 | — | 0 USD | 0 USD |
| phase 1, argon | 8 mondes × 2 parties × (16 questions + 3 cartes) = 304 | au plus 0,20637 USD par appel : coût d'un appel de proposeur de la course v67, génération 1 (`S1.M1.1.par_proposeur.argon.cout_proposeur_usd`) ; prix d'un appel de question à relever | 62,74 USD | — |
| phase 1, kimi | 304 | au plus 0,400484 USD par appel (`S1.M1.2.par_proposeur.kimi.cout_proposeur_usd`) ; prix d'un appel de question à relever | 121,75 USD | — |
| phase 1, total | 608 | — | 184,48 USD | 608 appels au plus haut prix observé (0,400484 USD), plus 10 % de reprises : **267,84 USD** |

Le prix d'un appel de question n'est dans aucun fichier lu : la borne prise est le coût d'un appel de proposeur de la course v67, qui écrivait 5 à 6 cartes par appel (`S1.M1.*.par_proposeur.*.cartes`) ; un appel de question a une sortie plus courte mais un historique croissant. Prix à relever avant le devis définitif.

**Nœud pour Lazar.**
- Décision : construire l'instrument du monde répondeur sans dépense, puis, sur devis, le jouer avec les deux proposeurs réels ?
- Enjeu : une mesure de la recherche des proposeurs indépendante de tout juge, qui mesure aussi sur la vérité le rendement tardif (C1) et la répartition entre raffiner et ouvrir (C3).
- Options : (a) phase 0 seule maintenant, phase 1 sur devis après lecture de la phase 0 — avantage : aucune dépense, R5 d'abord ; inconvénient : rien sur les proposeurs réels avant la phase 1. (b) phases 0 et 1 sous un seul devis (pire cas 267,84 USD) — avantage : calendrier ; inconvénient : dépense engagée avant de savoir si l'instrument ordonne les factices. (c) ne rien faire — avantage : aucun coût ; inconvénient : la composition reste sans instrument de recherche propre à côté de l'oracle de la boucle.
- Recommandation : (a), confiance ≈ 70 %. Défaut : aucun (la phase 1 est une dépense, nœud ; la note de conception est suspendue par la mère).

## P2 — Mémoire : mesurer la répétition de formes, puis essayer un indice de diversification (ligne C3)

**Ce que cela change, et où.** `pole/memoire.py`, par une version nouvelle (R12). Aujourd'hui l'identité d'une hypothèse est sa signature prédictive : divergence moyenne au plus 0,30 nat sur la sonde (l. 9-12, constante l. 34, garde `_garde_signature` l. 183-202). Deux cartes de même forme à paramètres différents ne sont donc pas une redite, ce qui est juste pour le juge, mais la mémoire ne voit pas la répétition de forme que l'analyse mesure. Trois options graduées :
- (i) **mesure seule** : la part de cartes qui répètent une forme (définition de l'analyse : arbre JSON de la loi, feuilles numériques masquées) est rapportée par génération et par proposeur dans le relevé ; aucun comportement ne change ;
- (ii) **indice servi** : la mémoire sert aux proposeurs la liste des formes déjà archivées (structure seule : ni paramètres, ni verdicts, ni témoins, conforme à la liste blanche, l. 3-5), avec la consigne de proposer une part de cartes de forme neuve ;
- (iii) **quota** : au plus q cartes d'une même forme par proposeur et par génération, au-delà un refus écrit (pas de repli silencieux).

**Pourquoi.** Nos journaux : mode dominant en S1 (9 sur 23, part 0,391304, `S1.M2.part`) et dans trois groupes sur quatre de S2 (`…M4.par_bras` : 0,414583, 0,32043, 0,359626 ; témoin de S2b 0,165945). L'article décrit les deux échecs, « DeepSeek-V4-Flash and Qwen3.6 open only 5.2-5.5 branches per game. » [PC-09, p. 8] ; « Over-exploration. GPT-OSS-120B opens 13.7 branches » [PC-10, p. 8] ; mais sa typologie est descriptive et ses arbres annotés par un modèle, « Recovery scores come from a panel of three LLM judges, and the search trees are annotated by an LLM. » [PC-11, p. 9] ; le sommet en U inversé n'est pas causal (lecture, section 1 C3).

**Ce qui reste différent.** Leurs branches sont des directions de questions dans un arbre fait par un modèle ; nos formes sont calculées par le code dans une grammaire fermée. En S2, raffiner les paramètres d'une même forme est exactement ce que l'attaque invite (bras retour plus haut que le témoin dans les deux sources) ; dans la boucle de production, raffiner une forme vraie peut être légitime : forcer la diversité peut tuer l'exploitation utile. Et le seuil d'un quart peut être atteint par la seule petitesse de la grammaire (11 formes pour 23 cartes).

**Essai sur monde planté.**
- **Phase 0 (sans dépense).** (a) Référence de construction : tirer au hasard, uniformément dans la grammaire servie, 23 cartes (et des suites de 16 essais), 10 000 fois (`SeedSequence(20261118)`), et calculer la même part. Critère fixé d'avance : si la médiane de la référence dépasse un quart, le mode dominant de S1 est un effet de la grammaire ; la ligne C3 se referme (ne change pas), rapporté. (b) Rejeu hors ligne des options (ii) et (iii) sur les 23 cartes de S1 : combien seraient refusées par (iii), sans vérité. (c) Proposeur scripté (`exemples/`, README section 6) sur mondes plantés, avec et sans quota, simulé ; calcul de puissance pour la phase 1. (d) Préalable : écrire la vérité par carte pour **toutes** les cartes, promues ou non, dans la lecture de course (écart E2 de l'analyse) ; c'est aussi ce qui manque pour mesurer C1 sur la boucle réelle.
- **Phase 1 (dépense, sur devis, seulement si la phase 0 ne referme pas la ligne).** Courses réelles à deux générations, bras témoin (mémoire actuelle) contre bras (ii), sur deux types de mondes plantés construits d'avance : D, lois vraies de formes absentes de l'archive (la diversité paie) ; E, lois vraies de formes déjà archivées à paramètres neufs (l'exploitation paie). Les deux types empêchent l'essai de construire sa conclusion. Cinq répétitions par bras et par type, mêmes mondes et mêmes graines dans les deux bras.
- Hypothèse : (ii) augmente les vraies découvertes de l'oracle par dollar sur D sans les baisser sur E.
- Mesure principale : vraies découvertes par dollar, au sens de l'oracle du monde planté (lois vraies plantées retrouvées et promues, témoins faux rejetés) ; secondaires : fausses promotions, part de formes répétées, formes distinctes.
- Critère fixé d'avance : (ii) retenue comme candidate (pas adoptée) seulement si, sur D, la différence est positive avec un intervalle à 95 % qui exclut 0, et si, sur E, la borne basse de la différence reste au-dessus d'une marge de non-infériorité gelée au préenregistrement, sans plus de fausses promotions. Sinon : ne change pas.
- Bras témoin : la mémoire actuelle, mêmes mondes, mêmes graines.

**Devis.**

| poste | unités | prix unitaire et source | estimation | pire cas |
|---|---|---|---|---|
| phase 0 | 0 appel | — | 0 USD | 0 USD |
| phase 1 | 2 bras × 2 types × 5 répétitions = 20 courses à deux générations | dépense d'une course à deux générations de la course v67 : 1,429736 + 0,564574 = 1,99431 USD, proposeurs et tests de mort (`S1.M1.1.depense_de_la_generation_usd`, `S1.M1.2.depense_de_la_generation_usd`) | 39,89 USD | 24 cartes par course au plus haut coût par carte observé, 0,129976 USD (`S1.M1.1.depense_de_la_generation_par_carte_usd`), plus 10 % de reprises : **68,63 USD** |

La dépense de S1 ne compte que les rôles proposeur et tests de mort (analyse, section 1) ; si la phase 1 joue aussi l'aiguilleur ou les juges croisés, leur prix est à relever. La taille (5 répétitions) est provisoire : la puissance se calcule en phase 0 (c), et le devis se refait si elle change.

**Nœud pour Lazar.**
- Décision : faire la phase 0 de P2 (référence de construction et rejeu hors ligne), puis, si la ligne C3 ne se referme pas, un essai payant de l'indice de diversification ?
- Enjeu : savoir si la répétition de formes de nos journaux est un défaut des proposeurs ou un effet de la grammaire, avant de toucher la mémoire.
- Options : (a) phase 0 seule, option (i) de mesure ajoutée au relevé — avantage : aucune dépense, peut refermer la ligne ; inconvénient : ne dit pas si un indice aide. (b) phase 0 puis phase 1 sous devis (pire cas 68,63 USD) — avantage : tranche sur l'oracle ; inconvénient : petite taille, puissance encore inconnue. (c) quota dur (iii) essayé à la place de (ii) — avantage : effet mécanique, sans consigne au modèle ; inconvénient : risque de tuer l'exploitation légitime (mondes E).
- Recommandation : (a), puis (b) seulement si la référence reste sous un quart ; confiance ≈ 75 %. Défaut : aucun (dépense en phase 1 ; note de conception suspendue).

## P3 — Candidats offerts au questionneur (lignes C2 et C4), montés sur l'instrument de P1

**Ce que cela change, et où.** Phases 0 et 1 : aucun module de la table 2 ; des bras ajoutés au jeu de P1. Une phase ultérieure toucherait le bisociateur ou la moisson (étapes 5 et 6 du README) ; elle n'est pas proposée ici.

**Les bras.** Avant la première question, le questionneur reçoit un panorama de formes candidates :
- A : seul (le bras de P1, partagé) ;
- B : panorama sans la forme vraie, un leurre de même famille à sa place, comme l'article le construit, « Cdecoy replaces it with a decoy, a real technique from the same family that the paper does not use, of similar length. » [PC-20, p. 15] ;
- C : panorama avec la forme vraie, **position tirée au hasard** (contrôle qui manque à l'article : lecture 2e ; « within Cfull , the line that names the core idea is asked about in 78-90% of games, against 45-67% for the lines within two positions of it » [PC-21, p. 16]) ;
- D (phase 2) : candidats extérieurs, la question proposée par l'autre proposeur sur le même historique, ordre tiré, choix par le questionneur (analogue du réservoir, « Each round, all four models independently propose a question from the same history, and one model picks among them. » [PC-04, p. 6]) ;
- A′ (phase 2, témoin à coût apparié) : le même proposeur fait deux propositions par tour et choisit (témoin *un modèle, vote à k, coût apparié* de N-045 v2, point 4).

**Pourquoi.** L'article conclut « Once the correct idea is in the hypothesis space, weak models recognize it; what they lack is the ability to put it there themselves. » [PC-22, p. 8] et en tire « enriching the search with externally sourced ideas and questions may be more effective than improving any single model's generation ability » [PC-12, p. 1] ; mais sa reconnaissance passe par le répondeur modèle et le panorama fuit par construction, « A survey constructed using the solution may itself reveal information about it. Excluding the survey from idea-card prompts restricts how this information reaches the card, but does not remove it from the questioning process. » [PC-06, p. 17] ; et le plus fort perd comme sélecteur, « 5.20 5.34 5.24 5.19 +1.04 [+0.74, +1.34] +1.09 [+0.87, +1.39] +1.07 [+0.79, +1.36] −0.59 [−0.90, −0.28] » [PC-08, p. 7]. Dans notre jeu, la fuite est contrôlée (B et C ne diffèrent que par une ligne, à position tirée), le score est la vérité, et le coût est mesuré, ce que l'article ne rapporte pas (lecture, section 1 C4).

**Ce qui reste différent.** Un modèle choisit ici quelle question poser parmi des candidats : c'est de la production, permise ; ce qui reste interdit, c'est qu'un modèle choisisse ce qui est promu, ou que la composition se choisisse sur un verdict (N-058). Le bras C contient la vérité par construction : C − B mesure la reconnaissance, jamais la découverte ; aucun panorama contenant une loi vraie connue, ni un témoin du pôle, n'est jamais servi dans la boucle de production (section 0, point 3).

**Mesures et critères (fixés d'avance).** Recouvrement à T = 16 (divergence à la vérité), par proposeur.
- C2 dans notre cadre : tient si C − B est positif avec un intervalle à 95 % qui exclut 0 pour chaque proposeur, et le reste une fois la position tirée prise en compte ; rapporté aussi : l'écart est-il plus grand pour le proposeur le plus faible (l'article l'affirme sur six points, lecture section 1 C2). Sinon : ne change pas.
- C4 dans notre cadre (phase 2) : D − A′ positif à coût apparié (recouvrement par dollar), intervalle à 95 % qui exclut 0. Sinon : ne change pas.
- Bras témoins : B pour C ; A′ pour D ; questionneurs factices de P1 (sans coût).

**Phase 0 (sans dépense).** Générateur de panoramas (leurres de même famille, longueur égale, position tirée), questionneurs factices qui reconnaissent par construction (choisissent la forme vraie si elle est présente) et qui l'ignorent : l'instrument doit mesurer C − B > 0 pour le premier et ≈ 0 pour le second (essai R5 sain et artefact).

**Devis.**

| poste | appels | prix unitaire et source | estimation | pire cas |
|---|---|---|---|---|
| phase 0 | 0 | — | 0 USD | 0 USD |
| phase 1 (B, C) | 2 proposeurs × 6 mondes × 2 bras × (16 + 3) = 456 | 0,20637 et 0,400484 USD par appel (mêmes sources que P1) ; prix d'un appel de question à relever | argon 47,05, kimi 91,31, total 138,36 USD | 456 appels au plus haut prix, plus 10 % : **200,88 USD** |
| phase 2 (D, A′), sur devis après la phase 1 | 2 proposeurs × 6 mondes × 2 bras × (2 × 16 + 3) = 840 | idem | total 254,88 USD | 840 appels au plus haut prix, plus 10 % : **370,05 USD** |

**Nœud pour Lazar.**
- Décision : essayer, dans l'instrument de P1, si nos proposeurs reconnaissent une forme vraie offerte (C2) et si des candidats extérieurs battent le proposeur seul à coût égal (C4) ?
- Enjeu : la seule voie de C2 et C4 qui se juge sur la vérité et le coût, sans juge ; elle conditionne toute idée de déplacer du budget vers des candidats extérieurs (bisociateur, moisson).
- Options : (a) phase 0 avec celle de P1, phase 1 sur devis après P1 phase 1 — avantage : réutilise l'instrument, aucun coût d'abord ; inconvénient : attend P1. (b) phase 1 et phase 2 ensemble (pire cas 570,93 USD) — avantage : C2 et C4 tranchés d'un coup ; inconvénient : la phase 2 est payée même si C2 ne tient pas. (c) ne pas faire P3 — avantage : aucun coût ; inconvénient : C2 et C4 restent indécidables.
- Recommandation : (a), confiance ≈ 65 %. Défaut : aucun (dépense ; note de conception suspendue).

## Ligne C1 : pas de proposition propre

C1 est indécidable ; la table prévoyait, si elle changeait, une borne de générations ou un déclencheur de diversification au plateau. Rien de tel n'est proposé : la mesure qui manque (rendement tardif sur la vérité, dans une même recherche) est prise par P1 (M-P1b) sur l'instrument et préparée par P2 (phase 0 d) sur la boucle réelle.

## Ce qui est écarté expressément

1. Un panel de juges modèles comme mesure de la recherche (le score de l'article, « Recovery scores come from a panel of three LLM judges, and the search trees are annotated by an LLM. » [PC-11, p. 9]) : remplacé partout par l'oracle du monde planté.
2. Classer des proposeurs, des bras ou des compositions par les promotions du juge statistique ou par le classement des juges croisés (N-058, point 1 et sa raison, l'invariant de N-053, point 5).
3. Un sélecteur modèle qui décide de la promotion d'une carte (le réservoir de l'article appliqué à la promotion) : contraire au principe de l'organisme (README, section 1).
4. Servir à un proposeur un panorama qui contient une loi vraie de la boucle ou un témoin (README, section 3 ; `memoire.py` l. 3-5).
5. La branche de C2 qui déplacerait du budget de la production vers des candidats extérieurs classés par les juges croisés : non proposée (C2 indécidable) ; si elle revient, elle se juge sur l'oracle et le coût (P3, phase 2).
6. Une borne de générations ou un déclencheur au plateau qui lirait le taux de promotion du juge : non proposé (C1 indécidable, et un tel signal ferait entrer un verdict de juge dans la conduite de l'organisme, ce que N-053 et N-058 bornent).

## Récapitulatif des devis (aucun n'est engagé)

| essai | phase sans dépense | phase payante proposée | pire cas |
|---|---|---|---|
| P1 | phase 0 (factices, R5) | phase 1, 608 appels | 267,84 USD |
| P2 | phase 0 (référence, rejeu, simulé, vérité par carte) | phase 1, 20 courses | 68,63 USD |
| P3 | phase 0 (factices) | phase 1, 456 appels ; phase 2, 840 appels | 200,88 USD ; 370,05 USD |

## Écarts et limites, déclarés

- Le préenregistrement d'analyse n'a pas été lu (hors de la liste) ; ses règles ne sont citées que par la table et la note d'analyse.
- Les colonnes 1 à 5 de la table remplie sont recopiées à l'octet de la table d'origine ; elles contiennent des passages entre guillemets qui ne sont pas de l'article (mots de Lazar, titre, libellés de verdict, noms de bras de l'organisme) : ils sont exclus de la vérification des guillemets, et la liste exacte est dans l'en-tête de la table remplie.
- Les prix unitaires sont des coûts observés par appel de proposeur et par carte de la course v67, pas des prix par appel de question ; ils sont marqués à relever.
- Les puissances des phases payantes ne sont pas calculées ; elles le seront en phase 0.
- Aucun accès réseau, aucune dépense, aucun appel de modèle, aucune machine.
