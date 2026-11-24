# Réponse à la question 5 : Carbon et le programme bâti sur ses réponses, contre Fable ; faut-il amender le Plan Turing ? (v1)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle, aucune course lancée.
- **Heure** : `2026-11-24T12:09:24Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`, branche `idees/questions-directeur-2026-11-24-v1`.
- **Fichiers lus** : `CLAUDE.md` (`dcd1e7ce…`) ; mandat (`ab6f19bb…`) ; demandes reformulées, question 5 (`52d1cc47…`) ; apport du directeur (`43716a8a…`) ; demande d'origine (`230585b9…`) ; `reponse-fable-max-v1.md` (`8ec4f9e0…`) et provenance (`85b171ec…`) ; les trois réponses de Carbon (`a9532fbb…`, `01f859c0…`, `3f92cede…`) et les deux questions de suite ; messages du lot 8 (`0a18a98e…`) ; rapport de priorités (`88d80f76…`) ; registre des soixante-deux idées, par recherche (`e7bf754c…`) ; réponse approfondie de Carbon sur la boucle, sections 0 à 2.2 (`f744320d…`) ; explication des mondes plantés (`895dbc0e…`) ; Plan Turing (`69c8deae…`) ; rapport du rang 1 du Pas 0 (`0a617ab1…`, verdict et section 2) ; note des hypothèses, lignes 550 à 620 (`5968ce0e…`) ; synthèse sur les puits étroits v2 et son erratum (`6112172f…`) et la demande 40 ; réponses aux questions 1 à 4 (en-têtes et verdicts) et 7 (en entier, `937e3e69…`) ; lignes R-5195 à R-5241 de `registres/decisions.md`, GO-2026-11-23-34 à -37 et GO-2026-11-24-01 de `registres/go.md`. Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **PDF téléchargés, hors dépôt** (droits), dans `/tmp/claude-0/-home-user-controle-ia-travail/72cb7e89-3107-5c40-8de3-bdb9cf3a5211/scratchpad/pdf-q5/` : `ovsjanikov-2012-functional-maps.pdf` (`7d7fb34a…`), `melzi-2019-zoomout-arxiv-1904.07865.pdf` (`ef5e4a21…`), `peyre-cuturi-solomon-2016-icml-v48.pdf` (`f72903b5…`). Refusé : PDF de Thompson 2014 (403).

## Verdict

Même architecture, trois écarts de fond : où se loge la cloche de la distance (naissance à optimum fixe chez Carbon, intérêt à optimum mobile chez Fable), le statut du mariage éloigné (soutenu, contre effet de queue), le contrôle des sources (Fable vérifie tout ; Carbon ne vérifie rien et se trompe trois fois). Le Plan Turing tient surtout sur des décisions du directeur ; le seul volet porté par un modèle seul, non vérifié, vient de Carbon et a déjà un échec. Amender peu, sans dépense : dire comment chercher dans un puits étroit, à deux niveaux. Confiance 0,7.

## 1. Ce que j'ai compris par « le programme élaboré ensuite »

Les pièces écrites du 23 novembre 15:15Z au 24 novembre 06:30Z : messages du lot 8, registre des soixante-deux idées, rapport de priorités, réponse de Carbon sur la boucle entre organisme et contrôle, explication des mondes plantés, Plan Turing, rapport du rang 1 du Pas 0. Ce programme n'est pas celui de Carbon seul : son rang 1 est l'épreuve de Fable (« le pont suit-il la carte ? », IDE-2026-11-23-027), son rang 2 celle d'Opus. J'ajoute la synthèse du 22 novembre sur les puits étroits, qui porte l'apport du directeur.

## 2. Conditions de la comparaison

| | Carbon | Fable |
|---|---|---|
| Questions reçues | trois : la demande, puis méta-espace et homomorphisme, rédigées après lecture de sa première réponse | une, sans rien lire des autres |
| Longueur | 4 451, 2 841, 3 095 mots ; la première dépasse la limite de 3 500 (R-5176) | 3 446 mots |
| Références | non vérifiées ; quelques « à vérifier » | 46 liens appelés, contenus classés (texte, résumé, source seconde), chiffres à la page |

L'inégalité interdit de juger Fable sur le méta-espace ou l'homomorphisme (jamais posés), de tenir un accord pour une preuve (même consigne en sept parties ; note l. 575-577), de conclure sur des modèles à partir d'une réponse chacun.

## 3. Tableau des écarts

| Thème | Carbon | Fable | Nature | Ce qui tranche |
|---|---|---|---|---|
| Objets | graphe multicouche : usage en attributs, structure typée projetée par π, social | hypergraphe daté à trois couches, plus les cadres M | vocabulaire surtout | question 7 |
| Surprise | `d = ½√JSD + (1−cos)/4`, poids posés | `S = −log p⁰`, modèle de surface appris avant t | fond : métrique arbitraire contre probabilité calibrée | chacune comme base, précision moyenne hors échantillon |
| Serrure et clé | `K = max κ·e^(−γχ)`, brut ; ensuite flèche envoyée sur chemin (foncteurs, résolvante) | `Z_r` centré réduit sous recâblage, rayons 1 et 2 | apport des deux : chemin et incompatibilités (C), nul intégré (F) | monde planté relation contre chaîne de deux (question 7) |
| Champ | `Σ α_m h_m(u)h_m(v)`, additif dans le préfacteur | `Σ Δh_k s_a(k)s_b(k)`, dans l'exposant | forme ; un catalyseur, non un champ (question 3) | les deux formes sur les découvertes multiples |
| Naissance | `(η₀C + η₁F)·σ(β₁K − β₂(d−μ)² − β₀)` | `p⁰·exp(βZ + γF)` | fond : cloche ou décroissance | spline de distance dans le modèle de Cox |
| Intérêt, profondeur | `I = d·K`, dérivation non donnée ; longueur de description ; PageRank × rupture | `I = q(S+W)`, W surprise retirée ailleurs | fond ; `d·K` croît sans borne avec d (fragile) | notation à l'aveugle, plan 2×2 (proposé par les deux) |
| Émergence | seuil : inverse de la plus grande valeur propre de la matrice sans retour [14] | branchement `n ≥ 1` ; `c_A·c_B = 1` | Carbon plus général, vérifié ; Fable, cas de Poisson | question 4 |
| Analogies | puits = écart d'énergie entre premier et second alignement ; polarisation gardée | puits = communauté ; polarisation écartée | vocabulaire ; Noether écarté trop vite par les deux (note l. 562-568) | — |
| Données | S2ORC, SciSciNet, révisions de Wikidata, Nobel, rétractations | PubTator 3 libre, SemMedDB, MeSH annuel, notes de Gu et Krenn, CHIMERA | apports propres ; erreur de Carbon sur les jumeaux (section 4) | — |
| Première expérience | SemMedDB, paires nées en 2018, fécondité seule ; contrôle par permutation des signes | PubTator 3, gel 2010 ; naissance contre vingt témoins, fécondité, cortège ; monde planté, permutation des types | fond : Carbon conditionne sur les paires nées, ne teste pas la naissance, mais se dit « sans biais du survivant » (erreur partielle) | fusion dans IDE-027 (amendement A3) |
| Oublis | coût d'épreuve, anomalies, effet Matthieu, abstractions nouvelles, réfutation rapide | public, problèmes, types, re-représentation, coût, négatifs, agents corrélés, niveau d'abstraction | accord sur quatre ; propres : Matthieu (C), agents corrélés et public (F) | — |

## 4. Désaccords de fait, à la source

1. **Mariage éloigné.** La source de Carbon dit l'inverse de son verdict « soutenue » : les stratégies risquées sont rares, une publication novatrice a plus de chances d'un fort impact, « mais la récompense supplémentaire ne compense pas le risque » [15, résumé]. Uzzi et collaborateurs : socle conventionnel et intrusion atypique [16, p. 468] ; Fleming : moyenne plus basse, variance plus haute [17, résumé] ; intérêt et distance entre chercheurs : ρ = −0,223 [18, v4 p. 8]. **Fable a raison** : effet de queue et d'interaction, non effet principal.
2. **Proximité aux nœuds.** Tranché par la question 2 : Gu et Krenn mesurent le parent (ρ = −0,166, [18, v4 p. 8]), pas l'idée fille. « Contredite » (Fable) et « soutenue » par l'unification et la rupture (Carbon) dépassent tous deux la source.
3. **Galison.** Carbon : rôle des horloges « démontré ». Le recenseur juge cet argument convaincant « less compellingly, in my opinion » [20]. **Fable a raison.**
4. **Transition topologique.** Carbon l'attribue à Bettencourt et collaborateurs 2008, *Scientometrics* 75(3), un modèle de population de type épidémique [21b, notice] ; la transition est dans Bettencourt, Kaiser et Kaur 2009 [21a], qui la placent après l'invention (question 4, manuscrit p. 5 et 14). **Erreur d'attribution de Carbon.** Seconde erreur : la méthode des jumeaux d'articles attribuée à Bikard, Murray et Gans 2015, dont le résumé traite de collaboration et de crédit chez 661 professeurs du MIT [22] ; la méthode est publiée par Bikard 2020 (texte de 2015 non lu : à vérifier).
5. **Forme de la distance optimale.** Aucune source ne départage optimum fixe et optimum mobile. La seule cloche mesurée qui porte sur l'intérêt est celle de la curiosité, maximale vers une confiance de 0,5 [19, p. 966] : elle soutient le lieu choisi par Fable (l'intérêt), non la mobilité. J'ai refait la dérivation de Fable : avec `g = ρ(1−q)(S+W) − 1`, `∂g/∂Z < 0` et `∂g/∂S > 0`, d'où `dS*/dZ > 0`, sous `β′ > 0` et W indépendant de S (hypothèse qu'il ne dit pas). Le `I = d·K` de Carbon n'a pas d'optimum intérieur. Épreuve : question 7.

## 5. Apports propres

**Carbon seul** : flèche sur chemin et incompatibilités (plausibles) ; seuil par la matrice sans retour (vérifié [14]) ; troisième couche et cinq signaux (fragiles : version lexicale réfutée, R-5241 ; un seul cas historique) ; Noether discret (vérifié par la note) ; écart du second alignement, permutation des signes (plausibles).

**Fable seul** : nul dans Z, ensemble à risque (plausibles) ; W (plausible, occupé, question 2) ; optimum mobile (dérivation vérifiée ici) ; cortège (une question, non un trou, règle R8) ; 46 références contrôlées (vérifié) ; agents corrélés (plausible).

## 6. Dépendances du Plan Turing

| Volet | Énoncés porteurs | Auteur | Vérification |
|---|---|---|---|
| 1, cartographie des verrous | anomalies et trous de preuve signalent où chercher | Carbon (méta-espace, section 2) ; oubli commun aux quatre modèles | version lexicale **réfutée** : aire sous la courbe 0,1667 sur 11 sous-domaines (rapport `0a617ab1…`) ; collecte : rappel 18 sur 20, rétrodiction 7 sur 8 (R-5228, petits effectifs) |
| | loi de Halberstadt | billet externe (GO-2026-11-24-01) | hors comparaison |
| 2, mathématiques nouvelles et Lean | cibles Q1 à Q6, théorème nu | programme antérieur ; Carbon en appui indirect (thématisation, Stitch) | indépendant des deux réponses |
| 3, Pas 0 et lot 8 | rang 1 | Carbon | réfuté sous forme lexicale |
| | IDE-027 | Fable | références vérifiées ; épreuve non courue ; seuils proposés |
| | IDE-028 | Opus | chiffres corrigés par la question 2 |
| | IDE-032 (macros) | Carbon | un seul cas historique ; date du dépôt vérifiée (question 7) |
| | IDE-033 (scissions) | Neon, H6 | à vérifier |
| | audit de Stitch et DreamCoder | Carbon | référence de Stitch « à vérifier » chez Carbon |
| | modèle d'avant 1900 | directeur | projet non identifié |
| 4, banc des mondes plantés | oracle planté et coût | N-058, N-076 (décisions) | décidé |
| | bilan du filtre, « × 21,5 » | Carbon (boucle, bloc A) | illustration sous suppositions, non opposable |
| 5, transfert | flux étanches | N-050, N-053, N-058, N-062 ; Carbon conforme | décidé |

**Sensibilité.** Sous la lecture de Carbon, IDE-027 garde son rang mais demande une spline ; sous celle de Fable, rien ne change. L'ordre tient. Seul le volet 1 repose sur un énoncé d'un seul modèle, et sa seule épreuve est négative.

## 7. L'apport du directeur : chercher dans un puits étroit

**Ce que prévoit le plan.** Le volet 1 dit où chercher, les mondes plantés et Lean comment juger ; rien sur comment chercher. Il ne cite pas non plus les décisions D1 à D5 du 22 novembre sur les puits étroits (synthèse v2, section 9).

**Deux niveaux à séparer.**
- *Quelle paire, quelle idée essayer.* Réglé le 22 novembre : sans minorant de la fréquence des bonnes idées, rien ne garantit de les trouver ; « forcer » se fabrique par un mélange défensif sur la grammaire publique, au prix de la force brute (D1, D2) ; les méthodes savantes sont des paris sur une structure.
- *Pour une paire, trouver la bonne correspondance φ.* Un problème d'affectation quadratique, que même l'approcher est difficile [8, résumé], dont le paysage a des puits étroits : l'écart du second alignement de Carbon en mesure la largeur. C'est ici que les méthodes candidates s'appliquent.

**Les méthodes, une par une.**
- **Partir des anomalies.** Conditionner sur un problème réduit l'espace : pari de structure, testable (prédictions P1 et P3 de la question 7) ; la forme de l'anomalie relève de la question 10.
- **Du grossier au fin par les modes propres.** Une application fonctionnelle est une matrice C entre deux bases de fonctions propres ; les contraintes y deviennent linéaires, l'estimation tient en « a single linear solve » [1, p. 2] ; C est compacte et presque diagonale pour des formes quasi isométriques [1, p. 3]. La montée spectrale raffine C [2, p. 1], mais exige une initialisation et échoue quand elle est mauvaise [2, p. 11, fig. 25]. L'appariement spectral de graphes ne s'approche de l'optimum que pour des graphes « suffisamment proches » [7, résumé]. Mon analyse : deux domaines éloignés ne sont pas quasi isométriques, c'est la définition du mariage éloigné ; et les modes grossiers d'un graphe de concepts codent communautés et popularité, comme les premières composantes des plongements codent la fréquence [23, p. 4]. Le grossier aligne d'abord la surface : il lisse le paysage sans rien garantir ; il faut des opérateurs typés, normalisés par le degré, et le nul de Z.
- **Relâcher, puis arrondir.** La distance de Gromov et Wasserstein [3] régularisée par l'entropie est non convexe et ne trouve qu'un point stationnaire, à coût `O(N₁²N₂ + N₂²N₁)` au lieu de `O(N₁²N₂²)` [4, p. 3-4] ; elle donne des correspondances souples [5]. L'arrondi n'a pas de garantie.
- **Recuit.** Convergence si et seulement si le refroidissement est logarithmique, `c/log(1+t)` avec c au moins la profondeur du plus profond minimum local non global [10, résumé] : temps exponentiel. Pics très étroits et pics très larges de masse comparable : mélange lent [11, p. 780] ; c'est le puits étroit lui-même. Relâcher, recuire et arrondir sont réunis depuis 1996 dans l'affectation graduée [6, résumé], que retrouve la régularisation entropique [4, p. 4] : antériorité (règle R8).
- **Chercheurs nombreux et divers.** Hong et Page supposent des meilleurs agents devenus semblables [12, résumé] ; leur démonstration est contestée [13, à vérifier]. Des proposeurs au corpus commun sont corrélés, ce qui dégrade toutes les bornes (synthèse v2, section 5) : la diversité se mesure (collisions, D3). Générer séparément, confronter ensuite (question 4).

**Verdict sur l'apport.** Un amendement, non une garantie : un banc de correspondances plantées, sur processeur, jugé selon N-058. Bras : base sans modèle (énumération, programme linéaire en nombres entiers exact sur petits voisinages, comme Carbon) ; criblage de Weisfeiler et Lehman, transport entropique à régularisation décroissante, arrondi ; spectral grossier-fin ; recuit ; proposeurs divers. Mondes : φ isolé près d'un leurre large de même masse ; relation contre chaîne de deux ; leurre de popularité (modes grossiers communs, structure fine différente : témoin qui doit tuer le bras spectral non normalisé). Mesure : φ retrouvés et coût par φ. Aucun bras ne se dit « forcer » (D1).

## 8. Amendements proposés (je propose ; rien n'est modifié)

| | Quoi | Pourquoi | Coût | Réversible | Nœud ? |
|---|---|---|---|---|---|
| A1 | Une section « comment chercher » à deux niveaux, qui renvoie à D1-D5 et rend obligatoire la base sans modèle (D2) | le plan est muet ; les décisions existent | nul | oui | non (décisions déjà prises) |
| A2 | Banc des correspondances plantées (section 7), au Pas 1 avec les mondes plantés, au Pas 0 si le créneau processeur le permet | seul moyen de juger les méthodes du directeur | 0 USD, quelques jours | oui | proposer avec recommandation (défaut sous 48 heures) |
| A3 | Dans IDE-027, avant scellement : spline de distance dans le modèle des naissances, permutation des signes à côté de celle des types | départage Carbon et Fable à coût nul | nul | oui avant scellement | non ; un nœud après scellement (écart) |
| A4 | Volet 1 et rang 1 : écrire que « les cinq signaux localisent les objets nouveaux » est un énoncé d'un seul modèle, réfuté sous forme lexicale ; toute version relationnelle passe d'abord par un monde de signaux plantés | règle R8, symétrie R4 | nul | oui | non |
| A5 | Errata de provenance au registre et dans les pièces qui citent Carbon : Bettencourt 2009, jumeaux de Bikard 2020, Galison non « démontré » | règle R7 | nul | oui | non |
| A6 | Volet 4 : les chiffres du bilan de Carbon sont des illustrations, jamais opposables | règle R6 | nul | oui | non |

**Ce qui ne doit pas changer** : la file critique de l'entretien du 1er décembre d'abord ; 0 USD au Pas 0 ; la règle N-058 (oracle planté et coût, jamais un juge) ; IDE-027 en tête ; le gel de l'organisme lourd ; D4 (le juge statistique ne guide pas la recherche en course).

## Références

1. Ovsjanikov, M., Ben-Chen, M., Solomon, J., Butscher, A. et Guibas, L. (2012). Functional maps: a flexible representation of maps between shapes. *ACM Transactions on Graphics* 31(4), 30. https://doi.org/10.1145/2185520.2185526 (PDF lu, p. 1-3)
2. Melzi, S., Ren, J., Rodolà, E., Sharma, A., Wonka, P. et Ovsjanikov, M. (2019). ZoomOut: spectral upsampling for efficient shape correspondence. *ACM Transactions on Graphics* 38(6). https://doi.org/10.1145/3355089.3356524 ; https://arxiv.org/abs/1904.07865 (PDF arXiv lu, p. 1, 2, 4, 11)
3. Mémoli, F. (2011). Gromov–Wasserstein distances and the metric approach to object matching. *Foundations of Computational Mathematics* 11(4), 417-487. https://doi.org/10.1007/s10208-011-9093-5 (notice)
4. Peyré, G., Cuturi, M. et Solomon, J. (2016). Gromov-Wasserstein averaging of kernel and distance matrices. *ICML 2016*, PMLR 48, 2664-2672. https://proceedings.mlr.press/v48/peyre16.html (PDF lu, p. 2-4)
5. Solomon, J., Peyré, G., Kim, V. G. et Sra, S. (2016). Entropic metric alignment for correspondence problems. *ACM Transactions on Graphics* 35(4). https://doi.org/10.1145/2897824.2925903 (résumé)
6. Gold, S. et Rangarajan, A. (1996). A graduated assignment algorithm for graph matching. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 18(4), 377-388. https://doi.org/10.1109/34.491619 (résumé)
7. Umeyama, S. (1988). An eigendecomposition approach to weighted graph matching problems. *IEEE Transactions on Pattern Analysis and Machine Intelligence* 10(5), 695-703. https://doi.org/10.1109/34.6778 (résumé)
8. Sahni, S. et Gonzalez, T. (1976). P-complete approximation problems. *Journal of the ACM* 23(3), 555-565. https://doi.org/10.1145/321958.321975 (résumé)
9. Kirkpatrick, S., Gelatt, C. D. et Vecchi, M. P. (1983). Optimization by simulated annealing. *Science* 220(4598), 671-680. https://doi.org/10.1126/science.220.4598.671 (notice)
10. Hajek, B. (1988). Cooling schedules for optimal annealing. *Mathematics of Operations Research* 13(2), 311-329. https://doi.org/10.1287/moor.13.2.311 (résumé)
11. Woodard, D. B., Schmidler, S. C. et Huber, M. (2009). Sufficient conditions for torpid mixing of parallel and simulated tempering. *Electronic Journal of Probability* 14, 780-804. https://doi.org/10.1214/EJP.v14-638 (résumé ; p. 780 vérifiée sur PDF par `verification-pdf-citations-puits-etroits-v1.md`)
12. Hong, L. et Page, S. E. (2004). Groups of diverse problem solvers can outperform groups of high-ability problem solvers. *PNAS* 101(46), 16385-16389. https://doi.org/10.1073/pnas.0403723101 (résumé)
13. Thompson, A. (2014). Does diversity trump ability? *Notices of the American Mathematical Society* 61(9), 1024. https://doi.org/10.1090/noti1163 (notice ; texte refusé, contenu à vérifier)
14. Karrer, B., Newman, M. E. J. et Zdeborová, L. (2014). Percolation on sparse networks. *Physical Review Letters* 113, 208702. https://doi.org/10.1103/PhysRevLett.113.208702 (résumé)
15. Foster, J. G., Rzhetsky, A. et Evans, J. A. (2015). Tradition and innovation in scientists' research strategies. *American Sociological Review* 80(5), 875-908. https://doi.org/10.1177/0003122415601618 (résumé)
16. Uzzi, B., Mukherjee, S., Stringer, M. et Jones, B. (2013). Atypical combinations and scientific impact. *Science* 342(6157), 468-472. https://doi.org/10.1126/science.1240474 (notice ; résumé lu par Fable)
17. Fleming, L. (2001). Recombinant uncertainty in technological search. *Management Science* 47(1), 117-132. https://doi.org/10.1287/mnsc.47.1.117.10671 (notice ; résumé lu par Fable)
18. Gu, X. et Krenn, M. Interesting scientific idea generation using knowledge graphs and LLMs. arXiv 2405.17044, v4. https://arxiv.org/abs/2405.17044 (chiffres de la v4 p. 8 lus par la question 2, non relus ici)
19. Kang, M. J. et al. (2009). The wick in the candle of learning. *Psychological Science* 20, 963-973. https://doi.org/10.1111/j.1467-9280.2009.02402.x (p. 966 lue par Fable, provenance)
20. Wald, R. M. (2004). Recension de *Einstein's Clocks, Poincaré's Maps*. *Physics Today* 57(9), 57. https://doi.org/10.1063/1.1809093 (page lue)
21. (a) Bettencourt, L. M. A., Kaiser, D. I. et Kaur, J. (2009). Scientific discovery and topological transitions in collaboration networks. *Journal of Informetrics* 3, 210-221. https://doi.org/10.1016/j.joi.2009.03.001 (manuscrit lu par la question 4) ; (b) Bettencourt, L. M. A., Kaiser, D. I., Kaur, J., Castillo-Chávez, C. et Wojick, D. E. (2008). Population modeling of the emergence and development of scientific fields. *Scientometrics* 75(3), 495-518. https://doi.org/10.1007/s11192-007-1888-4 (notice)
22. Bikard, M., Murray, F. et Gans, J. S. (2015). Exploring trade-offs in the organization of scientific work: collaboration and scientific reward. *Management Science* 61(7), 1473-1495. https://doi.org/10.1287/mnsc.2014.2052 (résumé, NBER w18958) ; Bikard, M. (2020). Idea twins. *Strategic Management Journal* 41, 1528-1543. https://doi.org/10.1002/smj.3162 (notice)
23. Mu, J., Bhat, S. et Viswanath, P. (2018). All-but-the-top. *ICLR 2018*. https://arxiv.org/abs/1702.01417v2 (p. 4 lue par Fable)
