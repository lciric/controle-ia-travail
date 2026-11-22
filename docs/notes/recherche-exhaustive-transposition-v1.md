# Recherche d'antériorité : transposer la stéganographie et la comptabilité des matières au contrôle de l'IA — v1

Date : 2026-11-22 (UTC). Classe C (note de travail). Règle R8 : « non trouvé » veut dire « non trouvé après la recherche décrite », jamais « libre ».
Sources lues sur PDF, empreintes à côté : `docs/sources/recherche-exhaustive-transposition-v1/` (17 PDF). Les pages citées sont celles du PDF.

## 1. Recherche faite

**Requêtes sur le web** (36 ; mode étendu pour la plupart) :
- Additivité (A), 12 requêtes : stéganographie par lots et stéganalyse groupée appliquées au contrôle ; comptabilité des matières (Avenhaus) et surveillance d'agents ; puissance qui ne dépend que du budget total ; tests séquentiels et processus e contre le sabotage ; sabotage diffus et somme cumulée ; contrôle « à faible enjeu » et Neyman-Pearson ; attaque répartie entre agents et invariance ; jeux d'inspection et contrôle de l'IA (deux formulations) ; tests toujours valides et modèles non fiables ; matière non comptabilisée et détournement prolongé ; somme des soupçons et fragmentation.
- Racine carrée (B), 14 requêtes : loi de la racine carrée et sous-performance stratégique ; communication couverte (Bash, Goeckel, Towsley) et agents ; taille d'échantillon de détection de la sous-performance (deux) ; stéganographie des modèles de langue et capacité (trois) ; faible probabilité de détection et divergence de Kullback-Leibler ; limites informationnelles du contrôle ; référence honnête estimée, gardien qui estime la loi de couverture (deux) ; écarts en racine de n non détectables ; citations de Ker par des articles sur les modèles de langue.
- Dépendance (C), 10 requêtes : collusion secrète ; attaque qui préserve la marginale entre agents ; sondes corrélées entre copies d'agents ; autocorrélation des soupçons ; suites de 2606.10456 ; Arias-Castro, Bubeck et Lugosi et groupes coordonnés ; statistiques de balayage et « higher criticism » entre copies ; statistiques de dépendance de la stéganalyse et actions d'agents ; faible probabilité de détection et collusion ; stéganalyse groupée de textes.

**Citations descendantes** (Semantic Scholar) : Ker et al. 2008, loi de la racine carrée (120 citants) ; Bash et al. 2013 (1 000 premiers citants) ; Wen et al. 2411.17693 (34) ; 2606.10456 (0 citant indexé). Échecs : Ker 2006 et 2007, Arias-Castro 2012, Avenhaus (quota dépassé ; OpenAlex épuisé) ; Google Scholar non joignable. Ces quatre arbres restent à faire.

**Lu sur PDF** : les 17 articles du dossier. Résumé seulement : 2602.23163, 2507.02737, 2609.24994, 2608.09069, 2606.07054, 2610.29178, 2604.03968, 2611.21832 (rien de pertinent pour A, B, C). Le billet de Greenblatt (Alignment Forum, 24 mars 2025) a été lu en ligne.

## 2. Objet A — lemme d'additivité

**Travaux trouvés**
- Tailor, « Audit the Whisper », 2510.04303v2, octobre 2025 : collusion stéganographique entre agents, information mutuelle d'une course à l'autre. Théorème 3 (p. 12) : sur K courses indépendantes, l'erreur de tout test est bornée par la divergence totale K·d (Pinsker et Le Cam). C'est une borne sur la divergence totale, en boîte noire. Elle ne porte pas sur la puissance d'une accumulation de scores et ne dit rien d'une répartition inégale.
- Ghanem, 2608.02698v1, août 2026 : collusion couverte dans des populations d'agents. La puissance de tout test y est bornée par la divergence totale, sous décomposition additive (p. 5, lecture du niveau 2 déjà au dépôt). C'est une borne supérieure, en boîte noire, et les résultats sont annoncés comme provisoires.
- Khilar, « The Limits of Query Monitoring against Distributed Model Extraction », 2610.13083v1, 9 octobre 2026 : proposition 3 (p. 5), le délai du meilleur test séquentiel vaut environ ln(1/α)/D ; martingales de test conformes. L'objet est l'extraction de modèle par des comptes, pas le sabotage d'agents.
- Li et al., « Watermark Forensics for Generative Models », 2607.13003v1, juillet 2026 (p. 1) : pour le filigrane, le total de l'information paie l'attribution et sa répartition paie la localisation. C'est une additivité au sens de l'information, hors de la surveillance.
- Wen et al., 2411.17693v1, novembre 2024 : cadre de la « menace distribuée » (p. 1) et crédence mise à jour au fil des tâches ; tâches corrélées laissées ouvertes (p. 10). Aucun énoncé d'invariance.
- Makins et al., 2607.07368v2, juillet 2026 : quand on répartit l'attaque entre plus d'agents, le maximum du soupçon baisse (effet de fragmentation, p. 1). Ils ne testent pas la somme.
- Griffin et al., « Games for AI Control », 2409.07985v2 (p. 10) : rapproche la surveillance de confiance des jeux d'inspection d'Avenhaus, pas de la balance des matières.
- Greenblatt, billet de mars 2025 : formulation informelle du risque comme « total des bits » qui sépare l'agent du bon modèle.
- Déjà au dépôt : 2601.20022 et 2607.11751.

**Verdict.** Voisin à citer, avec une différence nette : l'invariance exacte de la puissance de la somme des scores à la répartition dans le temps et entre agents, à budget et variance honnête fixés, n'a pas été trouvée pour des moniteurs d'agents de langue après la recherche décrite. Les bornes en divergence totale (2510.04303, 2608.02698) en occupent l'esprit en boîte noire. La comptabilité des matières (Avenhaus et Jaech 1981) n'est citée dans aucun travail de contrôle trouvé ; seuls les jeux d'inspection le sont.

**Ce qui en ferait une contribution reconnue.** L'énoncé est élémentaire : un relecteur dira « somme de décalages ». Il ne vaut que par trois choses.
1. Un énoncé adapté aux scores de sondes : décalage additif, variance honnête estimée, dépendance entre agents.
2. Une vérification sur de vrais agents que le sabotage agit comme un décalage additif du score, et que la variance honnête est stable entre agents. Une corrélation entre agents gonfle la variance de la somme.
3. Une mesure qui confronte la somme au maximum dans le montage de fragmentation de 2607.07368 : le lemme prédit une somme plate là où le maximum baisse.

## 3. Objet B — loi de la racine carrée et régime n/√m

**Travaux trouvés**
- Khilar, 2610.13083v1 : proposition 4 (p. 5). La campagne la plus difficile à voir est une inclinaison exponentielle du trafic honnête. Sa capacité « obéit à une loi de la racine carrée (Ker, 2007 ; Bash et al., 2013) », chiffrée sur des données réelles. Une rampe lente empoisonne l'étalonnage de tous les détecteurs (p. 1, 9-10). Il faut « protéger la référence » (p. 10). Le travail transpose donc la loi au suivi des usages des modèles de langue. Il touche à la référence estimée de façon empirique, sans régime n/√m.
- Tailor, 2510.04303v2 (p. 12) : adversaire constructif à taux ρ = c√d, qui atteint la borne K·d. C'est la structure de la racine carrée, sans citer Ker.
- Li et al., 2607.13003v1 (p. 24) : situe la loi de la racine carrée (Ker 2008, Bash 2012) par rapport aux filigranes des modèles génératifs et la distingue du régime linéaire.
- Pandey et al., 2610.25032v1, octobre 2026 : surveillance passive des messages entre agents ; le nombre de messages qu'un moniteur doit lire est fixé à une constante près (p. 1). Cite Ker et al. 2008.
- Wen et al., 2411.17693v1 (p. 18) : si l'agent rend la référence honnête plus suspecte, son « budget » de comportement suspect augmente. C'est le seul énoncé trouvé, qualitatif, sur une référence manipulée en contrôle.
- Sous-performance stratégique : aucune loi d'échelle (2512.07810, 2611.14950, 2508.00943, résumés).

**Verdict.**
- Pour la surveillance des modèles de langue en général : **occupé en partie** par 2610.13083. La loi de la racine carrée y est transposée et chiffrée, mais contre des utilisateurs qui extraient le modèle, pas contre un agent qui sabote.
- Pour le sabotage d'agents, la sous-performance stratégique et la faible probabilité de détection d'agents : **non trouvé après la recherche décrite**.
- Pour le régime n/√m avec référence estimée (Ker 2010) : **non trouvé** en contrôle de l'IA. 2610.13083 en montre le symptôme, la rampe qui empoisonne, sans la loi.

**Ce qui en ferait une contribution reconnue.**
1. Un énoncé où l'agent répartit son sabotage sous une divergence par action, et où m, la taille de la référence honnête, entre explicitement.
2. Une vérification que la référence honnête est indépendante de l'agent jugé : il ne doit pas pouvoir la nourrir (Wen, p. 18).
3. Une mesure de la frontière : dommage indétectable en fonction de n, à m fixé, puis de m, sur de vrais agents. La pente ½ doit être estimée, pas supposée.

## 4. Objet C — théorème négatif et statistiques de dépendance

**Travaux trouvés**
- Zhang et Gao, 2606.10456v2 : proposition 1 (p. 3), toute statistique de marginale a une puissance égale au taux de fausses alarmes. L'article revendique d'être le premier à traiter ce trou formellement (p. 1). Sur de vraies traces (p. 8), un agent Qwen 7B jugé par un moniteur Llama 3B, l'attaque est fabriquée au niveau des scores, pas jouée par l'agent. Il suppose un attaquant aveugle aux traits. Le cas est temporel, en boîte noire.
- Hu et Wang, 2607.11751v1 (déjà au dépôt) : la moitié négative, fragments localement bénins.
- Khilar, 2610.13083v1 : proposition 1 (p. 5), une campagne qui épouse la loi conjointe est indétectable. Un détecteur de comptes qui « bougent ensemble » rattrape les campagnes rembourrées (p. 1-2). C'est une statistique de co-élévation entre comptes, en boîte noire, sur données réelles.
- Rose et al., NARCBench et HELIOS, 2604.01151v5 : statistiques de groupe tirées des tests composites (p. 1, 3). L'« alignement d'activations » (p. 17) est une moyenne des cosinus entre agents qui bouge « même quand les scores individuels restent normaux ». C'est une boîte blanche entre agents, empirique, sans théorème.
- Xu et al., AcMAS, 2607.06807v1 (p. 4) : des activations corrélées entre agents compromis ; il s'agit d'injection et de propagation.
- 2611.10620v1 (p. 1) : statistiques de balayage en ligne sur les scores des agents. Les sondes de collusion lisent surtout la consigne donnée.
- Makins et al., 2607.07368v2 (p. 45) : dépendance positive mesurée du soupçon d'un commit à l'autre chez de vrais agents, traitée comme une nuisance.
- Lindner et al., 2512.22154v1 (p. 2) : des scores corrélés rendent la surveillance inefficace.
- Pandey et al., 2610.25032v1 (p. 5) : égaler la marginale de chaque tour ne suffit pas.
- Davies et al., 2502.14828v2 (p. 1) : attaques « indétectables point par point » d'une interface d'affinage.
- Motwani et al., 2402.07510 ; 2510.04303 ; 2608.02698 : information mutuelle entre courses, en boîte noire.

**Verdict.**
- Le théorème négatif est **occupé en contrôle de l'IA** : en boîte noire et dans le temps par 2606.10456, entre comptes par 2610.13083 (proposition 1), pour la composition par 2607.11751.
- Les statistiques de dépendance entre agents sur activations sont un **voisin à citer, avec une différence nette** : 2604.01151 et 2607.06807 les emploient de façon empirique, sans énoncé d'aveuglement des marginales ni attaque qui préserve la marginale.
- **Non trouvé après la recherche décrite** : l'unification temps et agents par groupes de permutations ; un agent réel qui préserve lui-même la marginale de ses scores de sonde ; un énoncé en boîte blanche.

**Ce qui en ferait une contribution reconnue.**
1. Un énoncé sur les scores de sondes, avec ses classes d'attaquant : permutation ou copule.
2. Une preuve, sur de vrais agents entraînés ou incités, que la préservation de la marginale est atteignable. C'est la réserve que 2606.10456 pose lui-même (p. 8).
3. Une mesure qui compare la co-élévation sur activations aux bases de 2604.01151 et de 2610.13083, sous la même attaque.

## 5. Ce que le programme peut écrire

- « Après la recherche décrite (section 1), nous n'avons pas trouvé d'énoncé, pour des moniteurs d'agents de langue, de l'invariance de la puissance d'une accumulation de scores à la répartition du sabotage ; des bornes en divergence totale existent en boîte noire (2510.04303, 2608.02698). »
- « La loi de la racine carrée a été transposée au suivi des usages des modèles de langue contre l'extraction répartie (2610.13083) ; nous l'étudions contre un agent qui sabote, avec une référence honnête estimée de taille m. »
- « L'aveuglement des statistiques de marginales est connu en contrôle (2606.10456, 2607.11751, 2610.13083) ; nous l'énonçons sur des scores de sondes et le mesurons sur des attaques jouées par de vrais agents. »
- Les origines : Ker 2006-2010, Filler-Ker-Fridrich 2009, Bash et al. 2013, Avenhaus et Jaech 1981, Arias-Castro et al. 2012, citées comme les sources des outils.

## 6. Ce qu'il ne peut pas écrire

- « Premier à transposer la stéganographie, ou la loi de la racine carrée, au contrôle de l'IA » : 2610.13083, 2510.04303 et 2606.10456 l'interdisent.
- « Premier traitement formel des attaques qui préservent la marginale », ou « premières statistiques de dépendance entre agents » : 2606.10456, 2604.01151 et 2610.13083 l'interdisent.
- « Zone libre » ou « inédit » pour l'un des trois objets.
- Tout chiffre de ces articles qui n'est pas vérifié à la page citée. Toute affirmation sur la descendance de Ker 2006 et 2007, d'Arias-Castro 2012 et d'Avenhaus : ces arbres de citations n'ont pas été parcourus.
- Que la comptabilité des matières n'a « jamais » été rapprochée du contrôle : seuls les jeux d'inspection ont été trouvés (2409.07985, p. 10), et la recherche n'a pas épuisé les sources.
