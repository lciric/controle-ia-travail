# Contre-vérification des sections Verdict, Essentiel 1-5, 1, 2 et 3 de `reponse-demande-reformulee-v1.md`

Contre-vérificateur neuf (Opus 5.5), 22 novembre 2026. Je n'ai pas modifié la note. Pages = page du fichier PDF, sauf mention contraire.

## A. Écarts, du plus grave au moins grave

1. **Verdict, point 2** : « sur un pic étroit que rien ne signale, un agent guidé par ses propres modèles fait *pire* que le hasard : 2 % contre 42 %… 73 % ». Le chiffre vient de « A Society of AI Scientists », p. 22 : un agent qui règle une réaction chimique simulée à quatre variables « fixated on an early mediocre peak ». Le PDF ne parle ni de pic étroit, ni d'absence de signal, ni d'un agent guidé par ses modèles. Ces traits appartiennent à Cang (2611.19841, p. 3 : 19/32 et 1/32 contre 82 %). La phrase fusionne donc deux études. Correction : « Et sur un réglage simulé à quatre variables, un agent seul s'est fixé sur un premier pic médiocre : optimum trouvé 2 % des fois, contre 42 % au hasard uniforme et 73 % pour une optimisation bayésienne. »

2. **Verdict, point 3** : « lien trouvé 1 fois sur 15 sans indice, 15 sur 15 avec ». La source est Puranam et al. 2025, p. 18 : GPT-4, sur le seul problème de l'usine, « used an analogy ». Sur l'autre problème, la même page donne 14 sur 15 *sans* indice. Le rapport neuro-psycho-linguistique précise aussi que la précision est d'environ 0,50 (p. 23). Le chiffre est donc généralisé à partir d'un seul problème. Correction : « (GPT-4, un problème : analogie employée 1 fois sur 15 sans indice, 15 sur 15 avec ; mais 14 sur 15 sans indice sur le second problème) ».

3. **§ 2.1, ligne « Vallée »** : « le seuil d'erreur a la forme σ(1−µ)^L = 1 (Wilke 2005, p. 14) ». Wilke 2005 n'a que 8 pages. La formule est l'éq. 34 de van Nimwegen et Crutchfield 2000, p. 14 (vérifié dans le PDF, et rapport « vallées », § 8). Correction : « (van Nimwegen et Crutchfield 2000, éq. 34, p. 14) ».

4. **§ 2.1, ligne « Solutions partielles »** : « avec mécanismes de diversité, temps en n^(k−1) puis jusqu'à 4^k (Dang et al. 2018, théorèmes 6 et 10) ». Les théorèmes 6 et 10 de Dang et al. donnent O(n^(k−1) log n) pour le (µ+1) GA *sans* mécanisme explicite. Le 4^k vient du tableau 2 de la synthèse de Sudholt (1801.10087, p. 25), avec des mécanismes explicites (îles, partage, distance maximisée) ; dans le PDF de Dang, 4^k n'apparaît que dans l'introduction. Correction : « le (µ+1) GA seul atteint O(n^(k−1) log n) (Dang et al. 2018, théorèmes 6 et 10) ; avec des mécanismes explicites de diversité, jusqu'à O(n log n + kn + 4^k) (synthèse de Sudholt, tableau 2, p. 25) ».

5. **§ 3, ligne 2611.23068** : « Sur sept méthodes d'évolution d'agents, la sélection distingue… 49,7 ± 1,9 % ». Le 49,7 % est mesuré sur un réservoir fixe de 100 candidats issus de Terminal-Bench v2.1, avec le sélecteur par score d'exécution à un déroulé (tableau 1, p. 7 ; p. 8). Ce n'est pas un résultat sur les sept méthodes. Par ailleurs, 62,1 % porte un écart type de ± 42,9 (p. 7), que la note omet. Correction : « Sur un réservoir fixe de 100 candidats (Terminal-Bench), la sélection par score d'exécution choisit le meilleur des deux 49,7 ± 1,9 % du temps, soit le hasard ; les régressions font 30,5 % du réservoir et 62,1 % (± 42,9) des candidats acceptés (p. 7-8) ».

6. **§ 3, ligne 2611.19108** : « à corpus fixe, le gain vient du graphe, pas du choix des articles ». Le PDF (p. 7) donne pour la construction du graphe à articles fixés 58 % et 64 %, avec p = 0,36 et 0,07 : ce n'est pas significatif. Le seul énoncé net est négatif (« no evidence that TEG-selected papers alone improve »). Correction : « à corpus fixe, le choix des articles n'apporte rien de démontré ; l'effet du graphe va dans le bon sens sans être significatif (58 % et 64 %, p = 0,36 et 0,07) ». Il faut aussi ajouter : par article, p = 0,13 (p. 5).

7. **§ 3, ligne 2611.21859** : « exception sur un quatrième, 30 sur 30 pour la référence ». Il y a cinq jeux. La référence fait 0/30 sur HNF4A, YY1 et JUND, mais 16/30 sur RXRA (14 effondrements sur 30, p. 9) et 30/30 sur CTCF. Correction : « 16 sur 30 sur un quatrième (RXRA) ; sur le cinquième (CTCF), 30 sur 30 pour la référence ».

8. **§ 2.1, ligne « Aucune »** : « n·exp(c·ε^(−1/2)) (Pemantle 2009, théorèmes 3.3 et 3.4) ». D'après le résumé p. 1 et la p. 10, cette borne ne vaut que pour p < 1/2 (théorème 3.4). Le théorème 3.3 (p = 1/2) donne Θ(ε⁻¹n). Le texte dit aussi « à un facteur 1−ε » et non « à ε ». Correction : « pour des Bernoulli de moyenne p < 1/2, s'approcher du meilleur chemin à un facteur 1−ε coûte au moins n·exp(c·ε^(−1/2)) (théorème 3.4, p. 10) ; pour p = 1/2, Θ(ε⁻¹n) (théorème 3.3) ».

9. **§ 2.1, ligne « Traits descripteurs »** : « mais une aiguille cachée dans une case rend le temps exponentiel (théorème 4.1, p. 3) ». La p. 3 dit que la couverture est bornée « irrespective of the fitness » (pour k = 1 et le nombre de uns), et que c'est l'*optimal-cover time* qui devient exponentiel. Ce n'est pas le théorème 4.1. Correction : « …en O(n² log n) pour le descripteur « nombre de uns » (théorème 4.1, p. 3) ; mais une aiguille dans une case rend exponentiel le temps pour trouver l'optimum de chaque case (même page, hors théorème) ».

10. **§ 3, paragraphe « Limite de calendrier »** : « le dépôt le plus récent visible sur arXiv date du jeudi 19 novembre, 16 h 18 UTC ». La table versée `releve-arxiv/table-20261114-20261122-v1.json` contient trois dépôts plus tardifs le même jour, dont 2611.26601v1 à 18:54:19Z. 16:18:26Z est la date de 2611.26343, le plus récent des textes *lus*. Correction : « 18 h 54 UTC (2611.26601) ».

11. **§ 2.1, ligne « Cible plantée »** : « Quatre phases : impossible, difficile, facile ». Il y en a trois de nommées. Les quatre phases de la p. 37-38 sont : indétectable paramagnétique, indétectable en grappes, difficile détectable, facile détectable. Plus loin, « dur pour toute recherche locale » : la p. 41 dit seulement que Monte-Carlo et le propagateur de croyances échouent, et que XOR-SAT planté « presents the same phenomenology ». L'absence de phase difficile en transition continue est aux p. 23 et 36, hors de la plage « p. 37-41 ». Enfin, le rapport (§ 10) précise : « une grande partie relève des prédictions de la physique, non démontrées », alors que la note place cela dans la colonne « Ce qui est démontré ». Correction : « Quatre phases (deux indétectables, une difficile, une facile) ; … dans la phase difficile, Monte-Carlo et le propagateur de croyances partis du hasard restent bloqués (prédiction de physique statistique, non démontrée en général ; p. 23, 36-41). Un problème planté d'équations à parité, qui présente la même phase, se résout par élimination de Gauss (p. 41) ».

12. **Essentiel 2 et § 2.1, ligne « Pic étroit »** : « Aucun ne vient du bruit : le bruit fait perdre les puits étroits », placé parmi les gains démontrés. La base est Wilke et al. 2001, expérimental, sur 12 paires sur 40, avec le résumé seulement. Woodard porte sur l'échantillonnage et sur des masses *comparables*. Ce n'est pas démontré en général. Correction (essentiel 2) : « …Aucun ne vient du bruit ; une expérience sur organismes numériques (12 paires sur 40, résumé seulement) montre même le plat l'emporter sur le haut sous forte mutation ».

13. **§ 2.1, lignes « Espace à distance » et « Vallée »** : Levernier et al. sont présentés comme démontrés. Le rapport dit « analyse avec vérification numérique, pas un théorème ». Bénichou et al. ne sont exacts qu'en dimension un (p. 35). Van Nimwegen et Crutchfield, c'est de l'analytique approché. Ajouter « (analyse et numérique ; exact en dimension un seulement) ».

14. **§ 2.1, renvois de pages hors convention** (« p. N = page du fichier ») : Lovász « p. 4 » et « p. 10 » sont les numéros imprimés ; les pages du fichier sont 5 et 11 (vérifié sur l'image). Bubeck « p. 607 » est le numéro imprimé ; la page du fichier est 7. Correction : « p. 5 et théorème 2.10, p. 11 » ; « théorème 4, p. 7 (imprimé 607) ». Pour Lovász, la borne suppose aussi un départ tiré de la loi stationnaire : ajouter « en moyenne, depuis un départ stationnaire ».

15. **§ 3, ligne Society** : « −0,39 point sur 10…, p. 29 et 65 ». Le chiffre est aux p. 29 et **66** (tableau, −0,39 [−0,60 ; −0,20]). La p. 65 porte sur la transmission des méthodes. Correction : « p. 29 et 66 ». Même ligne, « Les chaînes de citations ne sont pas plus profondes qu'un nul tiré au hasard » : la p. 34 dit « long citation chains… no deeper than expected under a recency-matched random null ». Correction : « Les longues chaînes de citations ne sont pas plus profondes qu'un nul au hasard apparié par date (p. 34) ».

16. **§ 3, ligne « Records mathématiques »** : « le procédé de recherche tient en trois phrases ». C'est vrai pour Katz-Tao (2611.19594, p. 2). Pour les caps (2611.19543), le rapport « systèmes », § 11, dit « construction à la main… aucune recherche automatique ». Correction : « Katz-Tao : certifié par vérificateurs exacts, procédé en trois phrases ; caps : construction à la main, sans recherche automatique ».

17. **§ 3, ligne Schur (2611.22032)** : « un solveur guidé par une structure connue atteint 207 ». Nuance perdue : la note de Rowley donnait déjà une partition à 207 (p. 8). Ajouter : « taille déjà atteinte dans la note de Rowley (p. 8) ».

18. **§ 2.2, Gideoni** : « l'invite d'expert fait passer l'évolution de 1 réussite sur 3 à 3 sur 3 ». Le PDF (p. 4) dit : sur l'empilement de cercles, retrouver la borne de Lange et al. « Reformuler… améliore toutes les méthodes plus que la recherche » s'appuie sur un seul problème, l'inégalité d'incertitude (p. 6). Ajouter « (empilement de cercles) » et « (un problème, l'inégalité d'incertitude) ».

19. **Essentiel 4 et Lecture d'ensemble du § 2.2** : « dans l'ordre des mesures ». Aucune source ne classe ces facteurs entre eux. Le rapport « vérificateur exact », point 4, dit seulement qu'ils « pèsent plus que la politique de recherche ». Correction : « Ce qui pèse plus que la politique de recherche : la formulation, les opérateurs, le bruit du juge ».

20. **Petits écarts.**
    - § 2.2 : la citation de « Mutation Without Variation » omet « individual » (« over 93% of individual mutations », p. 6).
    - § 3, débat 2611.20649 : « 40 à 87 fois » ; le PDF (p. 7) donne 40,6 à 86,7. Écrire « 41 à 87 fois ».
    - § 3, 2611.26011 : 100 sur 100 est pour PS⁻ ; PS⁺ fait 74 sur 100 (p. 10). Ajouter « (74 sur 100 sur la seconde cible) ».
    - § 2.1, Alon et al. : le résultat vaut pour des expanseurs réguliers, et l'accélération porte sur le mélange. Écrire « sur un expanseur régulier, le mélange accélère au plus d'un facteur 2 ».
    - § 2.1, Oliveto : pour l'élitiste, il s'agit de la longueur *effective* ℓ* = ℓ1 + d1ℓ2/d2.

## B. Contrôlé sur PDF et conforme

- Society : 2 %, 42 %, 73 %, citation mot pour mot ; `society-of-ai-scientists-v1.pdf`, p. 22.
- Society : 88 % contre 30 %, rétabli en partageant les lieux sans les scores ; p. 22.
- Society : 19,4 points, « only 1.0 pp better at equal cost » ; p. 25.
- Society : 46 paires, 87,0 % compatibles, six avant la prépublication ; p. 28 (et p. 29, 40/46).
- Society : 936 agents et 936 études, 35 laboratoires, douze semaines ; p. 1 et 3.
- Society : nouveauté −0,39 par deux juges Gemini ; p. 29.
- Pal et Reuveni : critère σ/⟨T⟩ > 1, p. 4 ; dominance de la reprise fixe, p. 3 ; `palreuveni2017.pdf`.
- Luby et al. : 192 ℓ(log ℓ + 5), théorème 5, p. 9 ; (1/8) ℓ log ℓ, théorème 7, p. 11.
- Oliveto et al. : théorèmes 3 (p. 9) et 13 (p. 19).
- Woodard et al. : corollaire 3.2 (p. 11), exemple 4.1 (p. 12), conclusion (p. 20).
- Lovász : théorème 2.10(b) (page du fichier 11).
- Bubeck et al. : théorème 4, √(Kt log t) ; page du fichier 7.
- Böhme et Paul : (ex − ex²)⁻¹, « much less than five times » ; p. 5.
- Bossek et Sudholt : théorème 4.1, p. 3 (sens à corriger, A9).
- Zdeborová et Krzakala : élimination de Gauss et XOR-SAT, p. 41.
- Addario-Berry et Maillard : théorème 1.1 et concavité, p. 2-4.
- Pemantle : théorèmes 3.3 et 3.4, p. 10 ; résumé, p. 1 (portée à corriger, A8).
- Gideoni et al. : 4/9 et 6/9 (p. 5), 1/3 et 3/3 (p. 4), formulation (p. 6).
- Oved et al., jetons : six fois, ≤ 5 % sur 12 de 15, 23 à 28 % ; p. 1.
- Oved et al., réévaluation : classement qui change avec le budget, p. 2 ; 3 transactions sur 300, p. 12.
- Gupta et al. : 0,023 et 0,678 après Holm, Finding 1 ; p. 8.
- Toledo et al. : 45,5 contre 39,8 (p. 9) ; « gain no advantage » (p. 7).
- Hill Sampling : « no significant difference », p. 6.
- Heuresis : « novel ideas never approach… », p. 1.
- Mutation Without Variation : 87 % et 93 %, p. 6.
- Zhang et al. 2024 : 500 requêtes, 100 000 ; p. 9.
- Si, Yang et al. 2026 : « same sampling budget », p. 5.
- Cang : 19/32, 1/32, 82 %, hasard calculé ; p. 3 et 7.
- Resolution Hypothesis : 49,7 ± 1,9, 30,5 %, 62,1 % ; p. 7-8 (portée à corriger, A5).
- Price of an Explanation : +9,22 ± 1,40, p. 6 ; citation de la p. 1.
- Coverage Selection Gap : +0,060 à +0,100 ; « at most +0.015 » ; p. 8.
- Matter of Representation : 100/100 et 0/100 (p. 10) ; 52 contre 23 (p. 11).
- Embedding-Map : 0,30 à 0,66 et 0,73 à 0,92 ; p. 7.
- Medina et Benton : 0/30 sur trois jeux, au moins 13/30 ; p. 9 (exception à corriger, A7).
- Kambhamettu et al. : 63 % [52 ; 73], 32 % ; p. 5-6.
- Zyskind : 8 à 70 % et 78 à 100 % ; tableau 4, p. 12.
- EpiCompass : 46,6 → 60,9 ; « Exploration errors decrease more modestly » ; p. 6-7.
- Ground, Iterate, Trace : citation, p. 1.
- Abelio : 6 mars et 1er avril, p. 17.
- Openhagen : 0,75, 0,25 et 0,35 ; p. 5.
- Débat : « never exceeds », 40,6 à 86,7 ; p. 7.
- Schur : 195 et 207 ; p. 7-8.
- Relevé arXiv : 71 requêtes et 132 articles (script et table versés).

## C. Non contrôlé

- Levernier, Bénichou, Doerr, van Nimwegen (p. 1), Gamarnik, Georgakopoulos, Burda, Qian, Lässig et Sudholt, et Jansen et Wegener via la synthèse : contrôlés contre le rapport seulement, faute de temps.
- FunSearch, informations supplémentaires (−245, −60, −100, 2/5) et AlphaEvolve (p. 17-18) : valeurs lues sur figure, non relues.
- Alpöge, OpenAI, bioRxiv (résumé seulement) : pages HTML non conservées dans les sources, ou PDF bloqué.
- Inventa (p. 20), Simplicity et BRED : contrôlés contre le rapport seulement.
- « 27 recherches » et « 1 543 entrées » : conformes au rapport hors arXiv, non recomptés.
- Hors périmètre, mais à signaler : l'essentiel 7 écrit « 46 redécouvertes indépendantes ». La p. 28 parle de 46 paires sur la même question, sans citation, dont 87 % compatibles. « Redécouvertes » exagère.
