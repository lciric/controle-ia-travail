# Réponse à la question 2 : la profondeur d'une idée comme surprise retirée ailleurs, la mesurer et l'exploiter dans l'organisme d'idéation (v1)

- **Nature** : pièce de travail (classe C). Aucune dépense, aucun appel à un modèle payant, aucune course lancée.
- **Heure** : `2026-11-24T10:01:55Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort maximal, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`, branche `idees/questions-directeur-2026-11-24-v1`.
- **Fichiers lus** : `CLAUDE.md` (`dcd1e7ce…`) ; mandat (`ab6f19bb…`) ; demandes reformulées, question 2 (`52d1cc47…`) ; `reponse-fable-max-v1.md` (`8ec4f9e0…`, parties 1, 2, 4 et références) et sa provenance (`85b171ec…`) ; intuitions du directeur, message 1 (`6f6397ee…`) ; `note-hypotheses-et-appuis-v1.tex` (`5968ce0e…`, lignes 215 à 249) et `verification-references-v1/bibliographie-verifiee-v1.py` (`7753b3cb…`) ; réponse de Carbon, sections 1 et 2.1 à 2.5 (`a9532fbb…`) ; réponse de Neon, passages sur la rupture et le biais rétrospectif, section 2.6 (`b86ac5d1…`) ; registre des soixante-deux idées, fiches sur la profondeur et sur l'épreuve « surface et structure » (`e7bf754c…`) ; `decision-N-058-v1.md` (`854f2724…`) ; explication des mondes plantés, sections 1 et 2 (`895dbc0e…`) ; lignes citant Gu et Krenn dans le rapport de priorités (`88d80f76…`) et la proposition de subvention (`ce7b3c2d…`). Rien d'ouvert sous `coffre/`, `docs/verdicts/`, `runs/`, `diag/`, `donnees/`.
- **Sources en ligne, lues ce jour** : Gu et Krenn, arXiv 2405.17044, fichiers PDF v3 (`48e552c5…`, même empreinte que dans la provenance de Fable) et v4 (`fcb49a05…`), notices Crossref et Zenodo ; pour les autres références, notice Crossref ou arXiv, et texte ou résumé (détail dans la liste). Deux hôtes refusés par le mandataire réseau : github.com (données d'évaluation de Gu et Krenn non inspectées) et pnas.org (texte de la revue non vu). Fichiers gardés hors du dépôt (droits des éditeurs).

## Verdict

Le fait tient, mais il est petit et porte sur le parent : sur 2 996 idées bâties sur une paire de concepts (4 451 notes, une par idée, 110 responsables), l'intérêt décroît avec le degré du concept de l'évaluateur, ρ = −0,166 [1, v4 p. 8] ; rien sur l'idée fille ni sur la surprise retirée ailleurs. Celle-ci se mesure (information mutuelle ponctuelle entre l'idée et des faits hors de son voisinage, terrain occupé depuis Friedman, Kitcher et Myrvold) ; dans l'organisme, mesure rapportée seulement, tant qu'un monde planté à portée connue ne l'a pas validée.

## 1. Le fait, à la source

**Versions.** arXiv 2405.17044 : v1 le 27 mai 2024, v3 le 7 janvier 2025, v4 le 24 septembre 2026 ; article des *Proceedings of the National Academy of Sciences* 123(46), e2611349123, en ligne le 9 novembre 2026 [1]. « 2024 » date la première prépublication (la v3, que cite Fable, est de 2025), « 2026 » l'article et la v4. Pages d'arXiv ci-dessous.

**Plan et effectifs.** 110 responsables d'équipe de la Société Max Planck ont reçu chacun 48 projets rédigés par GPT-4, 16 par condition : paire à fort impact prédit, paire au hasard, titres seuls [1, v4 p. 7]. La paire prend un concept chez l'évaluateur (A), un chez le collaborateur proposé (B) [1, v4 p. 4 et 12] ; l'idée n'est montrée qu'à l'évaluateur [1, v4 p. 5]. 4 451 notes recueillies sur 5 280 possibles, moyenne 2,403 sur 5 [1, v4 p. 7]. Les traits du graphe ne valent que pour les 2 996 idées bâties sur une paire [1, v4 p. 8 ; v3 p. 4]. Les deux chiffres du dépôt sont donc justes : 4 451 notes (Fable, d'après v3 p. 3), dont 2 996 idées sur paire (le registre). Deux erreurs du registre : le dépôt Zenodo de 3 gigaoctets est le graphe de connaissances (notice Zenodo), les notes sont annoncées sur GitHub [1, v4 p. 12] ; « notées en aveugle » n'est établi, dans les pages lues, que pour l'identité du collaborateur [1, v4 p. 5].

**Signe et taille.** Degré et PageRank de A : pentes négatives sur 50 classes égales (R² des moyennes de classe 0,480 et 0,474), mais au niveau de l'idée ρ de Spearman = −0,166 et −0,176 ; distance sémantique entre chercheurs, −0,223 [1, v4 p. 8]. La v3, que cite Fable, disait « strongly negatively correlated », sans coefficient [1, v3 p. 4] ; le −0,166 du registre vient de la v4. L'association est faible, environ 3 % de la variance des rangs (0,166², calcul de l'auteur), et se concentre dans les classes de plus faible degré [1, v4 fig. 4(c), p. 6 ; lecture visuelle, à refaire sur les données].

**Ce que le résultat n'établit pas.**
- Une cause : le degré de A va avec sa généralité, sa familiarité, la taille de son champ, peut-être la qualité du texte de GPT-4.
- Un fait sur la fille : l'hypothèse de la profondeur de l'idée fille (H7) veut la graine « immédiatement proche de concepts nœuds » après l'expérience (note, l. 226) ; Gu et Krenn mesurent le parent. « Contredite pour les nœuds » (Fable, partie 1) prend l'un pour l'autre.
- La profondeur ou la fécondité : une note d'intérêt personnel par idée, chacun usant de l'échelle à son seuil [1, v4 p. 11].
- L'exclusion de la pertinence pour soi : posée par les auteurs pour la distance [1, v4 p. 8 et 11], elle vaut à mon avis pour le degré (un concept très connecté de ma liste est général).
- La généralité : Max Planck seul, 104 évaluateurs sur 110 en sciences de la nature, 41,2 % des invités [1, v4 p. 7 et 11].

## 2. Trois grandeurs, séparées

1. **Centralité des parents** : degré, PageRank des concepts parents, graphe gelé avant l'idée. C'est ce que mesurent Gu et Krenn.
2. **Position de la fille** : où tombe l'idée ajoutée au graphe (chemins raccourcis entre communautés) ; après coup, sa centralité et son indice de rupture (Carbon, section 2.4), qui mesure l'éclipse des prédécesseurs dans les citations [2, 3] et dont la validité contre le jugement des pairs reste discutée [4, 5] : covariable, pas critère.
3. **Surprise retirée ailleurs (portée, W).** Pour un lecteur de loi P (modèle du public, lecteur figé, loi d'un monde planté), une idée x et des faits Y = (y₁, …, yₙ) hors de son voisinage : W(x ; Y) = log P(Y | x) − log P(Y), information mutuelle ponctuelle. **Avant l'épreuve**, sur une batterie scellée avant toute lecture des idées. **Après coup**, sur les faits révélés ensuite (faits plantés dévoilés par l'oracle, littérature postérieure à une date de gel), notée sur tout l'ensemble à risque, liens nés et non nés, en score séquentiel [6].

Trois propriétés élémentaires. **(i) Symétrie** : sous une même loi, W(x ; Y) = S(x) − S(x | Y), avec S = −log P ; la pertinence informationnelle est symétrique [7, manuscrit d'auteur, éq. (7)]. Retirer de la surprise ailleurs et « expliquer a posteriori pourquoi l'idée surprenait » (note, l. 226) sont une seule grandeur ; le biais rétrospectif [8] fausse S(x) reconstruite après coup : elle se scelle avant. **(ii) Borne** : W ≤ S(x). Paraphrase du connu et universel vide, peu surprenants, ne retirent presque rien ; le bruit a S élevée et W nulle ; le rapport W/S écarte les deux. Cela vaut pour un lecteur cohérent (monde planté), non pour un lecteur figé. **(iii) Décomposition** : W(x ; Y) = Σⱼ W(x ; yⱼ) + U, où U, l'unification de Myrvold, est ce que l'idée ajoute à la dépendance entre les faits [7, éq. (8) et (12)]. La formule de Fable, somme lien par lien (partie 2), omet U : « même loi en A et en C », sans valeur prédite, a U > 0 et une somme presque nulle.

**« Ailleurs » exclut** le lien et ses parents (c'est S) ; les faits qui nomment un parent ou un voisin immédiat ; ceux qui partagent avec le texte de l'idée des entités ou des mots au-delà d'un seuil fixé d'avance ; ceux qui ont servi à produire, choisir ou valider l'idée.

**La pondération par la centralité** (π chez Fable) fait revenir le nœud par la fenêtre : un changement près d'un nœud déplace beaucoup de termes lourds, et W pondéré se corrèle au degré des parents par construction. C'est un jugement de valeur, sans sens informationnel. W principal non pondéré, ou compté par classes de faits touchées (consilience de Whewell [9]) ; version pondérée en second, avec sa corrélation partielle au degré.

## 3. Trois estimateurs concurrents

| | E1. Lecteur figé, batterie contrastive | E2. Compression sur plusieurs bassins | E3. Réajustement du modèle de surface |
|---|---|---|---|
| Données | texte de l'idée ; batterie scellée de faits hors voisinage, chacun avec un faux apparié ; deux modèles ouverts de familles différentes, coupure antérieure aux faits | bassins encodés (relations typées, équations, programmes) ; schéma de l'idée ; bibliothèque des lois connues | graphe d'usage daté ; modèle de surface ajusté avant la date ; liens nés et non nés ensuite |
| Calcul | Σⱼ [log-cote(vrai contre faux \| x) − log-cote(vrai contre faux)] : terme à terme, la puissance explicative de Schupbach et Sprenger à une transformation monotone près [10, p. 108 ; théorème 2, p. 113] ; forme conjointe pour U | bits gagnés hors parents, bruts et nets du coût du schéma, relatifs à la bibliothèque courante, comme le progrès de compression [11, p. 3 et 5] ; par bibliothèque [12] ou sous-structures [13] | ajouter l'idée, réajuster, sommer les baisses de surprise hors voisinage (formule de Fable) |
| Coût, processeur | 3 000 idées × 100 faits : environ 13 millions de jetons, un jour par lecteur de moins d'un milliard de paramètres (estimation) | minutes à heures (estimation) | heures à jours |
| Bruit | texte long qui amorce la batterie | encodage qui crée un gabarit commun | le réajustement bouge aussi sous un lien au hasard |
| Paraphrase | idée qui redit les faits (filtre « ailleurs ») | loi connue renommée, si la bibliothèque est oubliée | sans objet |
| Biais rétrospectif | batterie choisie après les idées ; lecteur entraîné après les faits | bassins encodés en connaissant l'idée | les liens nés lisent aussi l'attention et l'influence de l'idée |
| Surprise de qui | du lecteur, non du public | de la bibliothèque | du dossier publié, la plus proche du public |

E3 a un défaut de fond (analyse de l'auteur) : un modèle local donne zéro hors voisinage, un modèle global fait de W une fonction de S et de la taille des communautés parentes, et sous une loi cohérente un lien nu ne retire jamais plus que sa propre surprise (borne ii). La portée vient du contenu de l'idée, non du lien : E1 et E2 d'abord ; E3 après coup, contre un nul.

**Antériorité (règle R8).** Unifier, c'est réduire le nombre de phénomènes indépendants à admettre [14, p. 15], dériver beaucoup avec peu de schémas d'argument [15, p. 514] ; l'unification est fausse quand un schéma peut accueillir toutes les conclusions [15, p. 529], d'où le faux apparié de E1. Consilience [9] ; unification bayésienne [7] ; valeur de confirmation de la surprise d'une unification [16, p. 3] ; puissance explicative comme baisse de surprise, après Good et McGrew [10, p. 108 et 114]. Surprise bayésienne, qui ne récompense pas la neige d'un téléviseur, à la différence de l'information de Shannon [17, éq. (4), p. 1296 ; p. 1298]. Information qu'un texte ajoute, mesurée par un prédicteur borné [18, 19, 20]. Longueur de description minimale [21, 22]. Surprise des combinaisons, prédictive de l'impact [23]. En deux recherches, je n'ai pas trouvé leur réunion sur des idées de recherche validée contre un monde planté : une question, non un trou établi.

## 4. Épreuves de l'instrument, avant tout usage

**Monde planté à portée connue.** Huit miniatures à vocabulaires disjoints ; une loi cachée, renommée, plantée dans k ∈ {1, 2, 4, 8} d'entre elles, des lois locales ailleurs. La portée vraie d'une fiche qui énonce la loi dans un bassin est le gain exact de vraisemblance, sur des faits tenus à l'écart, dans les k − 1 autres ; l'orchestrateur seul la calcule, qui tient la graine. Portée et centralité du parent sont croisées. E1 exige des miniatures rédigées en langue naturelle. Seuils proposés, à geler : corrélation de rang avec la portée vraie ≥ 0,7 ; réponse croissante en k ; corrélation partielle avec le degré du parent, à portée fixée, ≤ 0,1 en valeur absolue.

**Témoins à zéro** (sous le 95ᵉ centile du nul) : bruit de même longueur ; paraphrase d'une loi connue ; liste des faits de la batterie (doit tomber au filtre « ailleurs ») ; universel vide (« tout tend vers l'équilibre ») ; idée accrochée au nœud sans contenu.

**Permutation.** Mille réaffectations idée-bassins, types de relation permutés à degrés constants : l'association doit disparaître, sinon l'instrument lit la popularité.

**Lecteurs.** Deux familles, accord de rang ≥ 0,6 ; écart entre les deux sens de la symétrie (i) rapporté.

Processeur, quelques heures. Une garde échoue : instrument invalide, aucune lecture.

## 5. Usage dans l'organisme

- **Banc des mondes plantés** (miniatures à test de mort mécanique) : la portée y a un analogue sans lecteur, le gain au-delà du plancher des méthodes connues d'une fiche appliquée telle quelle aux autres mondes, tenus à l'écart de sa conception ; proche dans sa forme du juge au nul formé des lois connues (N-064, N-067, connus par `CLAUDE.md` seulement).
- **Mesure rapportée** : seul usage de W estimé (E1 à E3) avant validation.
- **Tri des fiches**, ensuite, en clé seconde parmi celles qui ont survécu à l'oracle : permis, la règle qui juge la composition des proposeurs sur l'oracle du monde planté et le coût (N-058) visant les agents, non les fiches ; minimum des deux lecteurs pour E1.
- **Signal d'exploration** (vers les bassins où la portée se concentre) : portée plantée seulement.
- **Jamais** : choisir un proposeur, une composition ou un rôle sur W estimé, ni en faire une récompense (« aucun score de moniteur ni de juge n'entre dans un signal d'entraînement ou de sélection de l'agent », N-053, point 5, cité par N-058).
- **Nœud pour toi, non tranché** : la portée plantée peut-elle entrer dans l'oracle qui juge les compositions ? La règle nomme structures retrouvées et témoins plantés ; pondérer par la portée change le critère.

**Risque de gonflement.** Un proposeur apprend vite à amorcer les mots de la batterie, lister des faits, écrire long, énoncer des universels vides, s'accrocher aux nœuds si π pèse, exploiter les tics d'un lecteur et, si W lui revient, sur-ajuster la batterie. Parades : batterie scellée, cachée, renouvelée à chaque génération, valeurs rendues grossies comme le réservoir réutilisable et l'échelle [24, 25] ; filtre « ailleurs » ; faux appariés ; deux lecteurs ; W jamais rendu aux proposeurs. Reste la voie indirecte : une mémoire qui garde les fiches de fort W les fait imiter (loi de Goodhart [26]) ; la mémoire s'indexe sur l'oracle, pas sur W.

## 6. Première épreuve peu coûteuse : la portée explique-t-elle l'effet du nœud chez Gu et Krenn ?

**Données.** Les 2 996 idées sur paire, avec note, évaluateur et texte (GitHub, contenu à vérifier) ; le graphe gelé en avril 2023 (Zenodo), antérieur aux idées, produites de septembre 2023 à février 2024 [1, v4 p. 4 ; tableau III, p. 20].

**Gardes, dans l'ordre.** (0) Reproduire ρ = −0,166 à 0,02 près, sinon arrêt. (1) L'instrument passe la section 4. (2) Sur les vraies idées, la dispersion de W estimé dépasse celle du nul par permutation, sinon « non concluant ».

**Mesure.** E1, deux lecteurs ouverts, coupure antérieure à 2024 ; par idée, cent titres d'articles de 2024-2025 (OpenAlex) des domaines de A et de B qui ne nomment ni A, ni B, ni leurs voisins immédiats ; faux apparié : un concept du titre remplacé, par règle, par un concept de fréquence voisine de la liste de Gu et Krenn.

**Prédiction.** Corrélation partielle de rang entre W estimé et la note, à degré, PageRank et citations de A, distance sémantique, longueur et évaluateur fixés : ≥ +0,05, borne basse de l'intervalle à 95 % (rééchantillonnage par évaluateur) > 0 ; et le coefficient du degré de A perd au moins un quart quand W entre.

**Réfutation.** Borne haute < +0,02, gardes tenues : la surprise retirée ailleurs, ainsi mesurée, n'explique pas l'intérêt au-delà du nœud, qui se lit alors comme pertinence pour soi (épreuve rivale : la fréquence de A dans les articles de l'évaluateur absorbe l'effet du degré). Un signe négatif net réfute aussi. **Indécidable** : W estimé corrélé au degré de A au-delà de 0,5 en valeur absolue.

**Puissance et coût.** Sans grappes, demi-largeur de l'intervalle ≈ 0,036 (1,96/√2996, calcul de l'auteur), plus large avec 110 évaluateurs : le seuil de 0,05 frôle la limite, puissance à calculer au préenregistrement ; tous les seuils sont à geler. Processeur seul, un à deux jours ; aucune dépense.

**Suite** : même mesure contre la fécondité après une date de gel ; dans l'organisme, portée plantée contre centralité des parents.

## Ce que cette réponse ne permet pas de conclure

- Qu'un instrument validé sur monde planté mesure « la profondeur » des savants : il mesure W tel que défini.
- Qu'un nul sur Gu et Krenn réfute « profondeur = W » : seulement que W explique l'intérêt personnel dans ce jeu.
- Que la surprise d'un lecteur figé soit celle du public, ni que les coûts estimés tiennent (aucun essai).

## Références

1. Gu, X. et Krenn, M. (2026). Generating interesting scientific ideas using knowledge graphs and LLMs: evaluations with 100 research group leaders. *Proceedings of the National Academy of Sciences* 123(46), e2611349123. https://doi.org/10.1073/pnas.2611349123 — prépublication arXiv 2405.17044, v3 (7 janvier 2025, titre « Interesting scientific idea generation… ») https://arxiv.org/abs/2405.17044v3 et v4 (24 septembre 2026) https://arxiv.org/abs/2405.17044v4 ; graphe : https://doi.org/10.5281/zenodo.13900962. (Fichiers PDF lus, pages citées ; texte de la revue non vu.)
2. Funk, R. J. et Owen-Smith, J. (2017). A dynamic network measure of technological change. *Management Science* 63(3), 791-817. https://doi.org/10.1287/mnsc.2015.2366 (notice et résumé)
3. Wu, L., Wang, D. et Evans, J. A. (2019). Large teams develop and small teams disrupt science and technology. *Nature* 566, 378-382. https://doi.org/10.1038/s41586-019-0941-9 (notice)
4. Bornmann, L., Devarakonda, S., Tekles, A. et Chacko, G. (2020). Are disruption index indicators convergently valid? *Quantitative Science Studies* 1(3), 1242-1259. https://doi.org/10.1162/qss_a_00068 (résumé : 120 179 articles jugés par les pairs ; une variante un peu meilleure que les autres)
5. Leibel, C. et Bornmann, L. (2024). What do we know about the disruption index in scientometrics? An overview of the literature. *Scientometrics* 129, 601-639. https://doi.org/10.1007/s11192-023-04873-5 (résumé : validité convergente non tranchée, biais de temps et de données)
6. Dawid, A. P. (1984). Statistical theory: the prequential approach. *Journal of the Royal Statistical Society, Series A* 147(2), 278-292. https://doi.org/10.2307/2981683 (notice)
7. Myrvold, W. C. (2003). A Bayesian account of the virtue of unification. *Philosophy of Science* 70(2), 399-423. https://doi.org/10.1086/375475 (résumé ; équations lues dans le manuscrit d'auteur, https://pitp.phas.ubc.ca/archives/CWSS/2003AprilPWIAS/Talks/myrvold-BayesianUnification%5B1%5D.pdf ; pages publiées à vérifier)
8. Fischhoff, B. (1975). Hindsight is not equal to foresight. *Journal of Experimental Psychology: Human Perception and Performance* 1(3), 288-299. https://doi.org/10.1037/0096-1523.1.3.288 (notice)
9. Thagard, P. (1978). The best explanation: criteria for theory choice. *The Journal of Philosophy* 75(2), 76-92. https://doi.org/10.2307/2025686 (notice ; définition de la consilience, « expliquer plus de classes de faits », lue dans une source seconde, page à vérifier)
10. Schupbach, J. N. et Sprenger, J. (2011). The logic of explanatory power. *Philosophy of Science* 78(1), 105-127. https://doi.org/10.1086/658111 (texte lu, p. 108, 113 et 114)
11. Schmidhuber, J. (2010). Formal theory of creativity, fun, and intrinsic motivation (1990-2010). *IEEE Transactions on Autonomous Mental Development* 2(3), 230-247. https://doi.org/10.1109/TAMD.2010.2056368 (prépublication de l'auteur lue, https://people.idsia.ch/~juergen/ieeecreative.pdf, p. 3 et 5, éq. (6) et (7) ; pagination publiée non vue)
12. Bowers, M. et al. (2023). Top-down synthesis for library learning. *Proceedings of the ACM on Programming Languages* 7(POPL), 1182-1213. https://doi.org/10.1145/3571234 (résumé)
13. Cook, D. J. et Holder, L. B. (1994). Substructure discovery using minimum description length and background knowledge. *Journal of Artificial Intelligence Research* 1, 231-255. https://doi.org/10.1613/jair.43 (résumé)
14. Friedman, M. (1974). Explanation and scientific understanding. *The Journal of Philosophy* 71(1), 5-19. https://doi.org/10.2307/2024924 (texte lu, p. 15)
15. Kitcher, P. (1981). Explanatory unification. *Philosophy of Science* 48(4), 507-531. https://doi.org/10.1086/289019 (texte lu, p. 514 et 526 à 529)
16. Castellani, E., Dardashti, R. et Dawid, R. (2025). Unification and surprise: on the confirmatory reach of unification. Prépublication. https://philsci-archive.pitt.edu/26916/ (texte lu, p. 3)
17. Itti, L. et Baldi, P. (2009). Bayesian surprise attracts human attention. *Vision Research* 49(10), 1295-1306. https://doi.org/10.1016/j.visres.2008.09.007 (texte lu, p. 1296 et 1298)
18. Xu, Y., Zhao, S., Song, J., Stewart, R. et Ermon, S. (2020). A theory of usable information under computational constraints. *International Conference on Learning Representations*. https://arxiv.org/abs/2002.10689 (résumé)
19. Hewitt, J., Ethayarajh, K., Liang, P. et Manning, C. D. (2021). Conditional probing: measuring usable information beyond a baseline. *Empirical Methods in Natural Language Processing*. https://arxiv.org/abs/2109.09234 (résumé)
20. Chen, H. et al. (2023). REV: information-theoretic evaluation of free-text rationales. *Annual Meeting of the Association for Computational Linguistics*, 2007-2030. https://doi.org/10.18653/v1/2023.acl-long.112 (résumé)
21. Rissanen, J. (1978). Modeling by shortest data description. *Automatica* 14(5), 465-471. https://doi.org/10.1016/0005-1098(78)90005-5 (notice)
22. Grünwald, P. D. (2007). *The Minimum Description Length Principle*. MIT Press. https://doi.org/10.7551/mitpress/4643.001.0001 (notice)
23. Shi, F. et Evans, J. (2023). Surprising combinations of research contents and contexts are related to impact and emerge with scientific outsiders from distant disciplines. *Nature Communications* 14, 1641. https://doi.org/10.1038/s41467-023-36741-4 (résumé)
24. Dwork, C. et al. (2015). The reusable holdout: preserving validity in adaptive data analysis. *Science* 349(6248), 636-638. https://doi.org/10.1126/science.aaa9375 (notice)
25. Blum, A. et Hardt, M. (2015). The Ladder: a reliable leaderboard for machine learning competitions. *International Conference on Machine Learning*, PMLR 37, 1006-1014. https://proceedings.mlr.press/v37/blum15.html (notice et résumé)
26. Manheim, D. et Garrabrant, S. (2018). Categorizing variants of Goodhart's law. Prépublication. https://arxiv.org/abs/1803.04585 (résumé)
